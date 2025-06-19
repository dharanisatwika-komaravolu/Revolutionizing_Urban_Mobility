from flask import Blueprint, request, jsonify
from processing import process_locations

api_routes = Blueprint('api_routes', __name__)  # Grouping routes under a Blueprint

@api_routes.route('/process-data', methods=['GET'])
def process_data():
    result = process_locations()  # Call data processing function
    return jsonify(result)

@api_routes.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save("locations.csv")  # Save uploaded file
    return jsonify({"message": "File uploaded successfully"})
