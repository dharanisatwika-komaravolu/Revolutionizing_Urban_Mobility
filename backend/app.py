# from flask import Flask, request, jsonify
# from flask_socketio import SocketIO
# import random

# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*")  # Enable WebSockets for real-time updates

# # Simulate GPS location updates (For real GPS, integrate a GPS API or mobile device input)
# @socketio.on('track_location')
# def send_location():
#     while True:
#         latitude = random.uniform(12.900, 12.950)  # Random latitude
#         longitude = random.uniform(77.550, 77.600)  # Random longitude
#         socketio.emit('update_location', {'latitude': latitude, 'longitude': longitude})
#         socketio.sleep(5)  # Send update every 5 seconds

# if __name__ == '__main__':
#     socketio.run(app, debug=True)



from flask import Flask
from flask_cors import CORS
from routes import api_routes  # Import API routes

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

app.register_blueprint(api_routes)  # Register API routes

if __name__ == '__main__':
    app.run(debug=True)




