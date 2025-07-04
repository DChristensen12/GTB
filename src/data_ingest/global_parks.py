#!/usr/bin/env python3
"""
Download park boundaries from OpenStreetMap via OSMnx
and save them to data/raw/global/parks_osm/
"""

import os
import geopandas as gpd
import osmnx as ox

# 1. Load your AOI polygon
aoi_path = 'src/data_ingest/aoi/california.geojson'
aoi = gpd.read_file(aoi_path)
polygon = aoi.unary_union

# 2. Define the OSM tag for parks
tags = {'leisure': 'park'}

# 3. Fetch park geometries within the AOI
print("Querying OSM for parks in AOI...")
parks = ox.features_from_polygon(polygon, tags)

# 4. Create output directory
out_dir = 'data/raw/global/parks_osm'
os.makedirs(out_dir, exist_ok=True)

# 5. Save to GeoJSON
out_geojson = os.path.join(out_dir, 'parks.geojson')
parks.to_file(out_geojson, driver='GeoJSON')
print(f"Saved park boundaries to {out_geojson}")

# 6.) Filter to only polyhonal parks before writing the Shapefile (changed to include all geometries)
# parks_polygons = parks[parks.geometry.type.isin(['Polygon', 'Multipolygon'])] # only keep polygons and multipolygons

# 7. Save all features as a GeoPackage (which supports mixed geometries)
out_gpkg = os.path.join(out_dir, 'parks.gpkg')
parks.to_file(out_gpkg, driver = 'GPKG')
print(f"Saved all park features to {out_gpkg}")
