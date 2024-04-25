import src.capture as capture
from flask import Flask, request, jsonify
import ee


app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    ee.Initialize(project = "ee-glorioussatria")
    return jsonify({'message': 'Welcome to the Earth Engine API!'})

@app.route('/capture', methods=['POST'])

def capture_image():

    # Get the request data
    data = request.get_json()
    north = data['north']
    south = data['south']
    east = data['east']
    west = data['west']
    
    # Capture the image
    url = capture.capture_image(north, south, east, west)
    
    # Return a response
    return jsonify({'message': 'Image captured', 'url': url})

