from database import cursor, db

class TowBike:
	def __init__(self, bike_id=None, location=None, time=None, picture_filePath=None):
		self.bike_id = bike_id
		self.location = location
		self.time = time
		self.picture_filePath = picture_filePath

	def save(self):
		cursor.execute("INSERT INTO towed_bike (bike_id, location, time, picture_filePath) VALUES (%s, %s, %s, %s)",
		(self.bike_id, self.location, self.time, self.picture_filePath))
		db.commit()

	def __repr__(self):
		return f"{self.bike_id:20}, {self.location:10}, {self.time}, {self.picture_filePath}"


