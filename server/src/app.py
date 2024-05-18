from flask import Flask, render_template, make_response
import os
import time
import geocoder
import requests
from datetime import datetime

app = Flask(__name__)

def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)

def get_temperature():
    location = geocoder.ip('me').latlng
    if not location:
        return "Unable to get location"
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.now()
    hour = now.hour
    response = requests.get(api_request)
    if response.status_code == 200:
        meteo_data = response.json()
        temp = meteo_data['hourly']['temperature_2m'][hour]
        return temp
    else:
        return "Unable to get temperature data"

@app.route('/')
def index():
    server_time = format_server_time()
    temp = get_temperature()
    context = {'server_time': server_time, 'temp': temp}
    template = render_template('index.html', context=context)
    response = make_response(template)
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
