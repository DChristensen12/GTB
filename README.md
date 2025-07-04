# Green to Blue

**Green to Blue** is a personal project that explores the intersection of environmental degradation, climate resilience, and data accessibility through the lens of geospatial analytics and machine learning. Originally focused on satellite imaging, the project has evolved to integrate a broad range of open-source datasets—including vegetation indices, air pollution, population density, protected areas, elevation, and sea level projections—to better understand how environmental burdens and resources are distributed across urban and coastal landscapes.

By leveraging publicly available Earth observation data from platforms such as Sentinel-2, Landsat, OpenWeatherMap, CPAD, and NOAA, this project analyzes spatial patterns in vegetation health, urban heat, pollution exposure, and shoreline vulnerability. Interactive maps and dashboards will visualize the relationship between these factors and demographic data, revealing insights into environmental equity, infrastructure resilience, and urban sustainability.

---

## Modules

The project is structured around three key modules:

**1. Urban Green & Blue Infrastructure Index**  
Maps neighborhood-level access to ecologically beneficial resources (trees, parks, water bodies) and evaluates their distribution against population density and demographic equity indicators.

**2. Urban Heat & Pollution Hotspots**  
Identifies regions most exposed to land surface temperature anomalies, PM2.5, ozone, and impervious surface expansion, with overlays of population and income to highlight climate injustice.

**3. Sea Level Rise Vulnerability in California**  
Visualizes coastal flood risks under multiple sea level rise scenarios using elevation models and shoreline overtopping maps, layered with infrastructure, schools, and protected lands.

The goal is to build a lightweight, interpretable, and visually compelling pipeline that combines geospatial data science with sustainability insight—highlighting both the power of open data and the importance of making environmental risks transparent. Through Green to Blue, I aim to blend technical skill with environmental awareness in a way that informs action and deepens understanding.

(Currently a work in progress — interactive visualizations and notebooks will be released in stages.)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DChristensen12/GTB.git
cd GTB
```

### 2. Set up your environment

conda env create -f environment.yml
conda activate gtb-env

(If you use mamba, feel free to swap it in for faster installs.)
3. Configure environment variables

Copy the template:

cp .env.example .env

Then fill in the .env file with your API credentials:

AIRNOW_API_KEY=
GOOGLE_API_KEY=
NOAA_TOKEN=
PO.DAAC_USERNAME=
PO.DAAC_PASSWORD=

Some data sources like NASA PO.DAAC also require a .netrc file to handle authentication.
Download All Raw Data

Once your environment is set up and .env is filled in, run:

bash src/utils/download_all_data.sh

This will automatically call all the data ingestion scripts under src/data_ingest/, downloading:

    Sentinel-2 NDVI

    OpenStreetMap + CPAD park data

    GPWv4 and ACS population datasets

    AirNow and OpenWeatherMap air quality & temperature data

    3DEP elevation tiles

    NLCD land cover

    NASA PO.DAAC sea level rise projections

All data will be saved to data/raw/ in their respective subfolders. This lets you regenerate the full raw dataset at any time with a single command.
Project Structure

GTB/
├── data/
│   └── raw/
│       ├── global/
│       ├── heat_pollution/
│       └── sea_level_rise/
├── src/
│   ├── data_ingest/
│   └── utils/
│       └── download_all_data.sh
├── .env.example
├── .gitignore
├── environment.yml
└── README.md

Commit & Push Changes

For example, if you update the README or utility scripts:

git add src/utils/download_all_data.sh README.md
git commit -m "Add utility script for downloading all raw GTB data"
git push origin main

### Final Notes

Green to Blue is still in development. I’ll be releasing cleaned datasets, Jupyter notebooks, and interactive dashboards (via Tableau) in stages. The ultimate goal is to make environmental data more approachable—something you can visualize, reason about, and use to drive informed decisions around equity and resilience.

This project blends my background in chemistry, geospatial analysis, and data science to explore how technical insight can support sustainable futures. Thanks for following along.