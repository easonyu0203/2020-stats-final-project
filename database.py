import mysql.connector

db = mysql.connector.connect(
	host='localhost',
	user='root',
	database='stats_final_project_2020',
	passwd='breaking0203'
)

cursor = db.cursor()