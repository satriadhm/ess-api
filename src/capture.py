import json
import ee

def capture_image(firstCoordinate, secondCoordinate, thirdCoordinate, fourthCoordinate):
    # Define the bounding box as a rectangle
    bounding_box = ee.Geometry.Rectangle([firstCoordinate,secondCoordinate,thirdCoordinate,fourthCoordinate], proj='EPSG:4326')

    # Create an image collection representing a single image at the specified location and zoom level
    image_collection = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA') \
        .filterBounds(bounding_box) \
        .sort('CLOUD_COVER')

    # Check if the image collection is empty
    if image_collection.size().getInfo() == 0:
        print("No images found for the specified bounding box.")
        return

    # Get the first image from the collection
    image = image_collection.first()

    # Clip the image to the defined location
    clipped_image = image.clipToBoundsAndScale(geometry=bounding_box)

    # Specify visualization parameters
    vis_params = {
        'bands': ['B4', 'B3', 'B2'],  # True Color (Red, Green, Blue)
        'min': 0,
        'max': 0.3
    }
    # Get the whole image URL
    image_url = clipped_image.getDownloadURL({
        'scale': 70,  # Adjusted to 70 meters
        'region': bounding_box,
        'crs': 'EPSG:4326'  # Specify the desired coordinate reference system
    })
    
    # Return the image URL
    return image_url
   

 
