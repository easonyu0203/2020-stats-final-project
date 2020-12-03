import mysql.connector
from database import cursor

# import os
# os.chdir('/Users/eason/Desktop/statistics/final-project')

DB_NAME = 'stats_final_project_2020'

def create_database():
	cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
	print(f'database create {DB_NAME}')
	

create_database()