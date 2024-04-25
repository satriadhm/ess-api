import ee
import json

# Authenticate to Earth Engine

def capture_image(latitude, longitude, zoom=12, output_file="output.json"):
    ee.Authenticate()
    ee.Initialize()
    # Define the coordinates
    location = ee.Geometry.Point(longitude, latitude)

    # Create an image collection representing a single image at the specified location and zoom level
    image = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
        .filterBounds(location) \
        .sort('CLOUD_COVER') \
        .first()

    # Get a URL to the image thumbnail
    thumbnail_url = image.getThumbUrl({
        'min': 0,
        'max': 3000,
        'dimensions': 512,
        'region': location,
        'format': 'png'
    })

    # Create a JSON object with the thumbnail URL
    result = {
        'thumbnail_url': thumbnail_url
    }

    # Save the JSON object to a file
    with open(output_file, 'w') as f:
        json.dump(result, f)

    print(f"Image captured and JSON file saved as {output_file}")
