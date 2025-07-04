#!/usr/bin/env python3
"""
Download sea level rise dataset into data/raw/sea_level_rise/
"""

import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load .env
load_dotenv()

# Load NASA Earthdata credentials
NASA_USERNAME = os.getenv("NASA_USERNAME")
NASA_PASSWORD = os.getenv("NASA_PASSWORD")

if not NASA_USERNAME or not NASA_PASSWORD:
    raise ValueError("Missing NASA_USERNAME or NASA_PASSWORD in .env")

# Output directory
out_dir = "data/raw/sea_level_rise"
os.makedirs(out_dir, exist_ok=True)

# NASA PO.DAAC file
SEA_LEVEL_URL = "https://podaac-tools.jpl.nasa.gov/drive/files/allData/merged_alt/L2/gdr/nrt/global_mean_sea_level/mean_sea_level_gmsl.csv"
out_path = os.path.join(out_dir, "mean_sea_level_gmsl.csv")

print("🌊 Downloading global mean sea level data from NASA PO.DAAC...")

try:
    r = requests.get(SEA_LEVEL_URL, auth=HTTPBasicAuth(NASA_USERNAME, NASA_PASSWORD), timeout=30)
    r.raise_for_status()
    with open(out_path, "wb") as f:
        f.write(r.content)
    print(f"Saved sea level data to: {out_path}")
except requests.exceptions.RequestException as e:
    print("Failed to fetch sea level data:", str(e))

