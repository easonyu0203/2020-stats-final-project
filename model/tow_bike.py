from database import cursor, db
import requests
from requests.exceptions import ConnectionError, HTTPError
import sys
import os.path as path

class TowBike:
	def __init__(self, bike_id=None, location=None, time=None, picture_url=None, _id=None):
		self._id = _id
		self.bike_id = bike_id
		self.location = location
		self.time = time
		self.picture_url = picture_url
		self.picture_filePath = ''
		self.picture_fileName = ''
		self.return_time = None


	def __eq__(self, other):
		return self.bike_id == other.bike_id and self.time == other.time

	
	def save_picture(self):
		"""store picture localy and init filePath & fileName"""
		try:
			res = requests.get(self.picture_url)
		except HTTPError as err:
			print(err)
			exit()
		except ConnectionError as err:
			print(err)
			exit()
		except:
			print("Unexpected error:", sys.exc_info()[0])
			exit()

		cursor.execute("SELECT MAX(ID) FROM towed_bike")
		index = cursor.fetchone()[0]
		index = 1 if not index else index + 1
		with open(f'./src/pictures/{index}.jpg', 'wb') as f:
			f.write(res.content)
		
		self.picture_fileName  = f'{index}.jpg'
		self.picture_filePath = path.abspath(f'./src/pictures/{index}.jpg')



	def save(self):
		"""return True if save else False (already have entry)"""
		# check if have entry already
		cursor.execute("SELECT COUNT(*) FROM towed_bike WHERE bike_id = %s AND time = %s", (self.bike_id, self.time))
		if(cursor.fetchone()[0] > 0):
			return False

		self.save_picture()

		cursor.execute("INSERT INTO towed_bike (bike_id, location, time,picture_url, picture_fileName, picture_filePath) VALUES (%s, %s, %s, %s, %s,%s)",
		(self.bike_id, self.location, self.time, self.picture_url, self.picture_fileName, self.picture_filePath))
		db.commit()

		return True


	def __repr__(self):
		return f"{self.bike_id:20}, {self.location:20}, {self.time}, {self.picture_fileName:20}, {self.picture_filePath}"


