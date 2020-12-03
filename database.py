import mysql.connector

db = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='breaking0203'
)

cursor = db.cursor()