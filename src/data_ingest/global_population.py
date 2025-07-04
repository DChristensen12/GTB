#!/usr/bin/env python3
"""
This Script is to Download GPWv4 population density rasters for multiple years
and save them to data/raw/global/population/
"""


import os
import requests

# List of Years to download
YEARS = [2000, 2005, 2010, 2015, 2020]

# Destination folder
OUT_DIR = "data/raw/global/population"
os.makedirs(OUT_DIR, exist_ok=True)

def download_year(yr):
    url = f"https://pacific-data.sprep.org/system/files/Global_{yr}_PopulationDensity30sec_GPWv4.tiff"
    out_path = os.path.join(OUT_DIR, f"pop_density_{yr}.tif")
    if os.path.exists(out_path):
        print(f"[SKIP] Already have {yr}")
        return
    print(f"[DOWN] {yr} from {url}")
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(out_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1024*1024):
            f.write(chunk)
    print(f"[OK] Saved to {out_path}")

if __name__ == "__main__":
    for year in YEARS:
        download_year(year)
