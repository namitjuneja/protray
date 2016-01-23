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
    weather_data = get_weather_record(request) #returns python dict with key as day and value another dict {"location" : location, "description" : description, "temp" : temp, "humidity" : humidity}
    for day in weather_data.keys():
    	if weather_data[day][temperature] < 5:
    		if weather_data[day][wind] < 
    	elif weather_data[day][temperature] >= 5 and weather_data[day][temperature] <= 30:
    	else:

    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)