import MySQLdb
from flask import request
import requests

db = MySQLdb.connect("sql6.freemysqlhosting.net","sql6103440","bqz3y1t3aU","sql6103440" ) # Open database connection


def add_location_record(request):
    details = {"timestamp" : request.form["timestamp"], "lat" : request.form["lat"], "lon" : request.form["lon"]}
    cursor = db.cursor() # prepare a cursor object using cursor() method
    sql = """INSERT INTO user_data (name, date, month, year, start_time, end_time, destination, contact, comments) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s);""", (str(request.form["name"]), str(request.form["date"]), str(request.form["month"]), str(request.form["year"]), str(request.form["start_time"]), str(request.form["end_time"]), str(request.form["destination"]), str(request.form["number"]), str(request.form["comments"]))
    cursor.execute(sql) # execute SQL query using execute() method.
    db.commit()
    db.close()  # disconnect from server

def add_weather_record(request):
    details = {"timestamp" : request.form["timestamp"], "lat" : request.form["lat"], "lon" : request.form["lon"]}
    cursor = db.cursor() # prepare a cursor object using cursor() method

    payload = {'lat': details['lat'], 'lon': details['lon'], 'appid': '4d6196e29e64cf28567f3089bbe34311'}
    r = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)
    response = r.json()
    weather_main, weather_desc, temp, humidity, wind_speed = '', '', '', '', ''
    city = 'Philadelphia'
    try:
        weather_main = response['weather'][0]['main']
        weather_desc = response['weather'][0]['description']
        temp = response['main']['temp']
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']

    except Exception as e:
        print e
        pass

    sql = """INSERT INTO weather_data (weather_main, weather_desc, temp, humidity, wind_speed, city) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s);""", (weather_main, weather_desc, temp, humidity, wind_speed, city)
    cursor.execute(sql) # execute SQL query using execute() method.
    db.commit()
    db.close()  # disconnect from server
