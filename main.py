from flask import Flask
import json

#models import
from location_update import add_location_record, add_weather_update

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/location')
def location():
    add_location_record(request)
    add_weather_update(request)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)