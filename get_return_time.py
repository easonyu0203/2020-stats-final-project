import os; os.chdir('/Users/eason/Desktop/statistics/final-project')
from database import cursor, db
from web_crawler import crawl_towbike_at
from datetime import date, timedelta, datetime
from model.tow_bike import TowBike


def main():
	"""check if any bike be returned from 2020/12/01 to today, if have any, then save return time to database"""

	web_towed_bikes = []
	start_day = date(2020, 12, 1)
	end_day = date.today()
	delta = timedelta(days=1)
	print('getting all entry from 2020/12/01 to today from website...')
	while start_day <= end_day:
		web_towed_bikes += crawl_towbike_at(start_day)
		start_day += delta

	db_towed_bikes = []
	print('get all entry from 2020/12/01 to today from mySQL...')
	cursor.execute("SELECT id, bike_id, time, return_time FROM towed_bike")
	for _id, bike_id, time, return_time in cursor.fetchall():
		db_towed_bikes.append(TowBike(_id=_id,bike_id=bike_id, time=time, return_time=return_time))
	print(f'web bike count: {len(web_towed_bikes)}')
	print(f'db bike count : {len(db_towed_bikes)}')
	print('check for update...')
	return_bikes = [bike for bike in db_towed_bikes if bike not in web_towed_bikes and bike.return_time is None]

	if return_bikes == []:
		print('(no update need)')
	else:
		for bike in return_bikes:
			cursor.execute("UPDATE towed_bike SET return_time=%s WHERE id=%s", (datetime.now(), bike._id))
		db.commit()
		print(f'(update {len(return_bikes)} entries)')


if __name__ == "__main__":
	main()
	