from database import cursor, db
import os.path as path

class TowBike:
	def __init__(self, bike_id=None, location=None, time=None, picture_filePath=None):
		self.bike_id = bike_id
		self.location = location
		self.time = time
		self.picture_filePath = picture_filePath
		self.picture_fileName = path.basename(picture_filePath)

	def save(self):
		"""return True if save else False (already have entry)"""
		# check if have entry already
		cursor.execute("SELECT COUNT(*) FROM towed_bike WHERE bike_id = %s AND time = %s", (self.bike_id, self.time))
		if(cursor.fetchone()[0] > 0):
			return False

		cursor.execute("INSERT INTO towed_bike (bike_id, location, time, picture_fileName, picture_filePath) VALUES (%s, %s, %s, %s,%s)",
		(self.bike_id, self.location, self.time, self.picture_fileName, self.picture_filePath))
		db.commit()

		return True


	def __repr__(self):
		return f"{self.bike_id:20}, {self.location:20}, {self.time}, {self.picture_fileName:20}, {self.picture_filePath}"


