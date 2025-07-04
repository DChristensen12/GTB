import os
import subprocess
from datetime import date, timedelta

NDVI_BASE_DIR = "data/raw/global/ndvi"
os.makedirs(NDVI_BASE_DIR, exist_ok=True)

# MODIS tile coverage for California + Western US
tiles = ["h08v04", "h09v04", "h10v04", "h08v05", "h09v05", "h10v05"]

start_year = 2004
end_year = 2024
interval_days = 16

base_url_template = "https://e4ftl01.cr.usgs.gov/MOLT/MOD13Q1.006/{year}.{doy:03d}/"

for year in range(start_year, end_year + 1):
    for doy in range(1, 367, interval_days):
        # Skip the invalid days (e.g., Feb 30)
        try:
            date(year, 1, 1) + timedelta(days=doy - 1)
        except ValueError:
            continue

        for tile in tiles:
            year_dir = os.path.join(NDVI_BASE_DIR, str(year))
            os.makedirs(year_dir, exist_ok=True)

            filename_prefix = f"MOD13Q1.A{year}{doy:03d}.{tile}.006"
            url = base_url_template.format(year=year, doy=doy)

            print(f"Fetching {filename_prefix} from {url}")

            cmd = [
                "wget",
                "--load-cookies", os.path.expanduser("~/.urs_cookies"),
                "--save-cookies", os.path.expanduser("~/.urs_cookies"),
                "--keep-session-cookies",
                "--auth-no-challenge=on",
                "--content-disposition",
                "--no-check-certificate",
                "--directory-prefix", year_dir,
                "--no-verbose",
                "--accept-regex", filename_prefix,
                "--reject", "index.html*",
                "--mirror",
                "--no-parent",
                "--cut-dirs=5",
                url
            ]

            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to fetch {filename_prefix} — {e}")
