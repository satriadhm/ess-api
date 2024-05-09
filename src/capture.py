import json
import ee
import geemap

def capture_image(firstCoordinate, secondCoordinate, thirdCoordinate, fourthCoordinate):
   
  # A Landsat 8 surface reflectance image.
    # A Landsat 8 surface reflectance image.
    image = ee.Image(
        'LANDSAT/LC08/C02/T1_L2/LC08_044034_20201028'
    ).select(['SR_B.'])  # reflectance bands

    # Define the region of interest using the provided coordinates.
    region = ee.Geometry.BBox(106.39607222222223,-6.6147361, 106.39625277777779,-6.6145556)

    # Define visualization parameters
    visParams = {
      'bands': ['SR_B4', 'SR_B3', 'SR_B2'],  # Use visible bands for RGB visualization
      'min': 0,  # Minimum pixel value
      'max': 3000,  # Maximum pixel value
    }

    # Set the export "scale" and "crs" parameters.
    task = ee.batch.Export.image.toDrive(
        image=image.visualize(visParams),  # Apply visualization parameters to the image
        description='image_export',
        folder='ee_demos',
        region=region,
        scale=30,
        crs='EPSG:5070'
    )
    
    task.start()
       
    return json.dumps({'status':'success', 'message':'Image has been captured successfully!', 'url': task.status()['state']})
