Green to Blue is a personal project that explores the intersection of environmental degradation, climate resilience, and data accessibility through the lens of geospatial analytics and machine learning. Originally focused on satellite imaging, the project has evolved to integrate a broad range of open-source datasets—including vegetation indices, air pollution, population density, protected areas, elevation, and sea level projections—to better understand how environmental burdens and resources are distributed across urban and coastal landscapes.

By leveraging publicly available Earth observation data from platforms such as Sentinel-2, Landsat, OpenWeatherMap, CPAD, and NOAA, this project analyzes spatial patterns in vegetation health, urban heat, pollution exposure, and shoreline vulnerability. Interactive maps and dashboards will visualize the relationship between these factors and demographic data, revealing insights into environmental equity, infrastructure resilience, and urban sustainability.

The project is structured around three key modules:

   1.) Urban Green & Blue Infrastructure Index
       Maps neighborhood-level access to ecologically beneficial resources (trees, parks, water bodies) and evaluates their distribution against population density and demographic equity indicators.

   2.) Urban Heat & Pollution Hotspots
       Identifies regions most exposed to land surface temperature anomalies, PM2.5, ozone, and impervious surface expansion, with overlays of population and income to highlight climate injustice.

   3.) Sea Level Rise Vulnerability in California
       Visualizes coastal flood risks under multiple sea level rise scenarios using elevation models and shoreline overtopping maps, layered with infrastructure, schools, and protected lands.

The goal is to build a lightweight, interpretable, and visually compelling pipeline that combines geospatial data science with sustainability insight—highlighting both the power of open data and the importance of making environmental risks transparent. Through Green to Blue, I aim to blend technical skill with environmental awareness in a way that informs action and deepens understanding.

(Currently a work in progress — interactive visualizations and notebooks will be released in stages.)


### API Key Setup

This project uses external APIs. To use them:

1. Copy the example file:
   ```bash
   cp .env.example .env
