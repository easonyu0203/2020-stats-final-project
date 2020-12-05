import os; os.chdir('/Users/eason/Desktop/statistics/final-project')
import os.path as path
from database import cursor #save data to mySQL
import requests
from requests.exceptions import ConnectionError, HTTPError
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
from model.tow_bike import TowBike
import sys
from getURL import crawl_url, max_page_index, craw_host_url


def get_TowBikes(url):
	"""get tow bikes from this url returm array of TowBike"""
	print(f"crawling {url}")
	try:
		res = requests.get(url)
	except HTTPError as err:
		print(err)
		exit()
	except ConnectionError as err:
		print(err)
		exit()
	except:
		print("Unexpected error:", sys.exc_info()[0])
		exit()


	soup = BeautifulSoup(res.text, 'html.parser')
	raw_TowBikes = soup.select("ul.violation-list>li")

	# if raw_TowBikes == []:
	# 	print('none entry to save to mySQL...')
	# 	return 0
	# if std_output:
	# 	print("saving entries to mySQL...")
	tow_bikes = []
	for raw_towbike in raw_TowBikes:
		bike_id = raw_towbike.select("div.info>h4>span")[1].text 
		location = raw_towbike.select("div.info>p")[0].text 
		raw_time = raw_towbike.select("div.info>p")[1].text
		time = datetime.strptime(raw_time, "%Y/%m/%d %I:%M:%S %p")
		picture_url = craw_host_url + raw_towbike.figure.a['href']
		bike = TowBike(bike_id, location, time, picture_url)
		tow_bikes.append(bike)

	tow_bikes.reverse()
	
	return tow_bikes


def crawl_towbike_at(date):
	"""get tow bike at this date return array of tow bike"""
	print(f'crawling towed bike at date {date}')
	max_index = max_page_index(date)
	if max_index == -1:
		print("there is no data to crawl...")
		return []

	tow_bikes = []
	for page_index in range(max_index, 0, -1):
		tow_bikes += get_TowBikes(crawl_url(date, page_index))
	
	return tow_bikes


def main():

	tow_bikes = crawl_towbike_at(date.today())

	add_entries_count = 0
	for bike in tow_bikes:
		if bike.save(): add_entries_count += 1

	print(f'(add {add_entries_count} entries)') if add_entries_count > 0 else print('(no entry add)')

	
if __name__ == "__main__":
	main()
