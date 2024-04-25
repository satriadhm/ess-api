import src.capture as capture
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/capture', methods=['POST'])

def capture_image():

    # Get the request data
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    zoom = data.get('zoom', 12)
    output_file = data.get('output_file', 'output.json')
    
    # Capture the image
    capture.capture_image(latitude, longitude, zoom, output_file)
    
    # Return a response
    return jsonify({'message': 'Image captured and JSON file saved as {output_file}'})

