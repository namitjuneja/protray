from flask import Flask
import json

#models import
from location import add_location_record, add_weather_update

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#uodate routes
@app.route('/location')
def location():
    add_location_record(request)
    add_weather_record(request)
    return json.dumps(data)

#template creation route
@app.route('/1/weather')
def location():
    add_location_record(request)
    add_weather_update(request)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)