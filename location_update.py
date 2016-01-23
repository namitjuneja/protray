import MySQLdb
from flask import request

db = MySQLdb.connect("sql6.freemysqlhosting.net","sql6103440","bqz3y1t3aU","sql6103440" ) # Open database connection


def add_location_record(request):
	details = {"timestamp" : request.form["timestamp"], "lat" : request.form["lat"], "lon" : request.form["lon"]}
	cursor = db.cursor() # prepare a cursor object using cursor() method
	sql = """INSERT INTO user_data (name, date, month, year, start_time, end_time, destination, contact, comments) 
		VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s);""", (str(request.form["name"]), str(request.form["date"]), str(request.form["month"]), str(request.form["year"]), str(request.form["start_time"]), str(request.form["end_time"]), str(request.form["destination"]), str(request.form["number"]), str(request.form["comments"]))
	cursor.execute(sql) # execute SQL query using execute() method.
	db.commit()
	db.close()  # disconnect from server

def add_location_record(request):
	details = {"timestamp" : request.form["timestamp"], "lat" : request.form["lat"], "lon" : request.form["lon"]}
	
	cursor = db.cursor() # prepare a cursor object using cursor() method
	sql = """INSERT INTO user_data (name, date, month, year, start_time, end_time, destination, contact, comments) 
		VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s);""", (str(request.form["name"]), str(request.form["date"]), str(request.form["month"]), str(request.form["year"]), str(request.form["start_time"]), str(request.form["end_time"]), str(request.form["destination"]), str(request.form["number"]), str(request.form["comments"]))
	cursor.execute(sql) # execute SQL query using execute() method.
	db.commit()
	db.close()  # disconnect from server