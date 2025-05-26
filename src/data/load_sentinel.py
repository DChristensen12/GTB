import ee

# Authenticate and initialize Earth Engine session
ee.Initialize()

def download_sentinel_ndvi(region_coords, start_date, end_date, export_name):
    """
    Downloads an NDVI image from Sentinel-2 data using Google Earth Engine
    and exports it to the user's Google Drive.

    Args:
        region_coords (list): Polygon coordinates [[lng, lat], ...]
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        export_name (str): Filename prefix for the exported .tif
    """

    # Define the region of interest as a polygon geometry
    region = ee.Geometry.Polygon(region_coords)

    """ Filter Sentinel-2 surface reflectance image collection
        - Covers the specified region
        - Within the provided date range
        - With less than 10% cloud cover
        - Use median composite to reduce cloud/shadow noise"""
    collection = (ee.ImageCollection("COPERNICUS/S2_SR")
                  .filterBounds(region)
                  .filterDate(start_date, end_date)
                  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))
                  .median())

    # Compute NDVI using NIR (B8) and Red (B4) bands
    ndvi = collection.normalizedDifference(['B8', 'B4']).rename('NDVI')

    # Create the export task to send the NDVI image to Google Drive
    task = ee.batch.Export.image.toDrive(
        image=ndvi,
        description=export_name,
        folder='GTB_Exports',  # This folder will be created in Google Drive
        fileNamePrefix=export_name,
        region=region,
        scale=10,              # Sentinel-2 resolution in meters
        crs='EPSG:4326',       # Standard lat/lon projection
        maxPixels=1e13         # Required for large image exports
    )

    # Start the export task
    task.start()
    print(f"Export task started: {export_name}")
