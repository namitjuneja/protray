import MySQLdb
from flask import request

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
    sql = """INSERT INTO user_data (name, date, month, year, start_time, end_time, destination, contact, comments) 
    VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s);""", (str(request.form["name"]), str(request.form["date"]), str(request.form["month"]), str(request.form["year"]), str(request.form["start_time"]), str(request.form["end_time"]), str(request.form["destination"]), str(request.form["number"]), str(request.form["comments"]))
    cursor.execute(sql) # execute SQL query using execute() method.
    db.commit()
    db.close()  # disconnect from server

def extract_date_from_timestamp(timestamp):
    #returns date
def get_weather_record(request):
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    weather_details = {} #key = date, value = {"location" : location, "description" : description, "temp" : temp, "humidity" : humidity, "wind" : wind}
    cursor = db.cursor() # prepare a cursor object using cursor() method
    # sql = """INSERT INTO user_data (name, date, month, year, start_time, end_time, destination, contact, comments) 
    # VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s);""", (str(request.form["name"]), str(request.form["date"]), str(request.form["month"]), str(request.form["year"]), str(request.form["start_time"]), str(request.form["end_time"]), str(request.form["destination"]), str(request.form["number"]), str(request.form["comments"]))
    sql = """SELECT * FROM eventList WHERE  `date` BETWEEN '2013-03-26 00:00:01' AND '2013-03-26 23:59:59'"""
    cursor.execute(sql) # execute SQL query using execute() method.
    # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      location = row[0]
      timestamp = row[1]
      description = row[2]
      temp = row[3]
      humidity = row[4]
      if weather_details[extract_date_from_timestamp(timestamp)] not in weather_details:
        weather_details[extract_date_from_timestamp(timestamp)] = {"location" : location, "description" : description, "temp" : temp, "humidity" : humidity, "wind" : wind}
      db.close()  # disconnect from server
      return weather_details
