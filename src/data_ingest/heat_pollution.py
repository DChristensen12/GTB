#!/usr/bin/env python3
"""
Download heat & pollution datasets:
- air quality (AirNow, Google AQ)
- demographics (US Census)
- elevation (Mapzen/Tilezen)
- land cover (NLCD 2016)
- temperature (NOAA GHCND)

Saves to: data/raw/heat_pollution/<layer>/
"""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

try:
    import mercantile
except ImportError:
    raise ImportError("mercantile is required for elevation tiles (pip install mercantile)")

# Load keys
load_dotenv()
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")
NOAA_TOKEN     = os.getenv("NOAA_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Optional

BASE_OUT = "data/raw/heat_pollution"

### ---------------- AIR QUALITY ---------------- ###
def download_airnow():
    print("Fetching current air quality from AirNow…")
    url = "https://www.airnowapi.org/aq/observation/latLong/current/"
    params = {
        "format": "application/json",
        "latitude": 34.0522,
        "longitude": -118.2437,
        "distance": 25,
        "API_KEY": NOAA_TOKEN
    }
    out_dir = os.path.join(BASE_OUT, "air_quality")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "airnow_current_la.json")
    r = requests.get(url, params=params)
    r.raise_for_status()
    with open(out_path, "w") as f:
        f.write(r.text)
    print("Saved AirNow data to", out_path)

def download_google_aq():
    if not GOOGLE_API_KEY:
        print("Google Air Quality API not yet configured. Skipping.")
        return

    print("Fetching Google Air Quality (not implemented yet)…")
    # TODO: Insert Google AQ fetch logic
    pass

def download_air_quality():
    print("\nStarting air quality downloads")
    try:
        download_airnow()
    except Exception as e:
        print(f"Failed to fetch AirNow: {e}")
    download_google_aq()

### ---------------- DEMOGRAPHICS ---------------- ###
def download_demographics():
    print("\n👥 Downloading demographics (ACS5 population by tract)…")
    if not CENSUS_API_KEY:
        raise ValueError("Set CENSUS_API_KEY in your environment")
    url = "https://api.census.gov/data/2020/acs/acs5"
    params = {
        "get": "NAME,B01003_001E",
        "for": "tract:*",
        "in": "state:06",
        "key": CENSUS_API_KEY
    }
    out_dir = os.path.join(BASE_OUT, "demographics")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "population_acs5_ca.json")
    r = requests.get(url, params=params)
    r.raise_for_status()
    with open(out_path, "w") as f:
        f.write(r.text)
    print("Saved demographics data to:", out_path)

### ---------------- TEMPERATURE ---------------- ###
def download_temperature():
    print("\n🌡️ Downloading daily max temperature from NOAA (LAX station)…")
    if not NOAA_TOKEN:
        raise ValueError("Set NOAA_TOKEN in your environment")
    url = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
    headers = {"token": NOAA_TOKEN}
    params = {
        "datasetid": "GHCND",
        "datatypeid": "TMAX",
        "stationid": "GHCND:USW00023169",
        "startdate": "2023-01-01",
        "enddate": "2023-12-31",
        "limit": 1000
    }
    out_dir = os.path.join(BASE_OUT, "temperature")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "ghcnd_usw00023169_tmax_2023.json")

    try:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        with open(out_path, "w") as f:
            f.write(r.text)
        print("Saved temperature data to:", out_path)
    except Exception as e:
        print(f"⚠️ NOAA fetch failed: {e}")

### ---------------- LAND COVER ---------------- ###
def download_land_cover():
    print("\n🌍 Downloading NLCD 2016 land cover data…")
    url = "https://s3.amazonaws.com/mrlc/nlcd_2016_land_cover_l48_20210604.zip"
    out_dir = os.path.join(BASE_OUT, "land_cover")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "nlcd_2016.zip")

    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, stream=True)
        r.raise_for_status()
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(1024 * 1024):
                f.write(chunk)
        print("Saved land cover to", out_path)
    except Exception as e:
        print(f"⚠️ Land cover download failed: {e}")

### ---------------- ELEVATION ---------------- ###
def download_elevation():
    print("\n⛰️ Downloading elevation tiles (Mapzen z=8)…")
    bbox = (-124.482003, 32.528832, -114.131211, 42.009518)
    out_dir = os.path.join(BASE_OUT, "elevation")
    os.makedirs(out_dir, exist_ok=True)

    print("Preparing tile download...")
    for tile in mercantile.tiles(*bbox, zooms=8):
        url = f"https://s3.amazonaws.com/elevation-tiles-prod/geotiff/{tile.z}/{tile.x}/{tile.y}.tif"
        out_path = os.path.join(out_dir, f"{tile.z}_{tile.x}_{tile.y}.tif")
        if os.path.exists(out_path):
            continue
        try:
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                with open(out_path, "wb") as f:
                    for chunk in r.iter_content(1024 * 1024):
                        f.write(chunk)
                print(f" • Saved tile {tile.z}/{tile.x}/{tile.y}")
        except Exception as e:
            print(f"⚠️ Tile {tile.x},{tile.y} failed: {e}")
    print("Elevation tiles done")

### ---------------- MAIN ---------------- ###
def main():
    print("Starting heat_pollution data ingest :)")
    download_air_quality()
    download_demographics()
    download_temperature()
    download_land_cover()
    download_elevation()

if __name__ == "__main__":
    main()
