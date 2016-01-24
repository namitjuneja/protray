from flask import Flask, request
import json

#models import
# from location import add_location_record, add_weather_update
from data_extractor import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#uodate routes
# @app.route('/location')
# def location():
#     add_location_record(request)
#     add_weather_record(request)
#     return json.dumps(data)

# #template creation route
# @app.route('/1/weather', method=["GET", "POST"])
# def location():
#     weather_data = get_weather_record(request) #returns python dict with key as day and value another dict {"location" : location, "description" : description, "temp" : temp, "humidity" : humidity}
#     for day in weather_data.keys():
#     	if weather_data[day][temperature] < 5:
#     		if weather_data[day][wind] < 8:
#     			return "a"
#     		else:
#     			return "a"
#     	elif weather_data[day][temperature] >= 5 and weather_data[day][temperature] <= 30:
#     		if weather_data[day][wind] < 8:
#     			return "b"
#     		else:
#     			return "b"
#     	else:
#     		if weather_data[day][wind] < 8:
#     			return "c"
#     		else:
#     			return "c"

#     return json.dumps(data)

@app.route('/week')   #returns all events from the current week
def week():
	# week_data = get_data()
	paragraphs = form_paragraphs()
	body = [{"type" : 1, "content" : "It was a foggy morning and I reached airport abput 2 hours ahead pf my flight. Because of low traffic the uber I booked just took 20 minutes for me to recah the airport and costed me about $5."}]
	return json.dumps({"username" : "Namit Juneja", "time_range" : "week", "body" : body})

@app.route('/day')   #returns all events from the current week
def day():
	pass
if __name__ == '__main__':
    app.run(debug=True)