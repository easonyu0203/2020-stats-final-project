import os; os.chdir('/Users/eason/Desktop/statistics/final-project')
import os.path as path
from database import cursor #save data to mySQL
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from model.tow_bike import TowBike
from src.env import last_content, craw_page_url, craw_host_url

def get_TowBikes(url):
	"""get tow bikes from this url and save to db
	return number of entry add"""
	res = requests.get(url)
	if(res.status_code != 200):
		with open('./mail.txt', 'a') as f:
			f.write(datetime.now()+"\n")
			f.write(f"can't get data!!\n")
			f.write(f"url: {url}\n")
			f.write(f"status code: {res.status_code}\n")
			f.write("\n")
		return
	soup = BeautifulSoup(res.text, 'html.parser')
	raw_TowBikes = soup.select("ul.violation-list>li")

	if raw_TowBikes == []:
		return 0
	print("saving to mySQL...")
	new_entry_count = 0
	for raw_towbike in raw_TowBikes:
		bike_id = raw_towbike.select("div.info>h4>span")[1].text 
		location = raw_towbike.select("div.info>p")[0].text 
		raw_time = raw_towbike.select("div.info>p")[1].text
		time = datetime.strptime(raw_time, "%Y/%m/%d %I:%M:%S %p")
		picture_url = craw_host_url + raw_towbike.figure.a['href']
		filePath = store_picture(picture_url)
		bike = TowBike(bike_id, location, time, filePath)
		if(bike.save()):
			new_entry_count += 1

		print(bike)
	
	return new_entry_count

	

def store_picture(url):
	"""store picture localy and return path to file"""
	res = requests.get(url)
	if(res.status_code != 200):
		with open('./mail.txt', 'a') as f:
			f.write(datetime.now()+"\n")
			f.write(f"can't get picture!!\n")
			f.write(f"url: {url}\n")
			f.write(f"status code: {res.status_code}\n")
			f.write("\n")
		return

	cursor.execute("SELECT MAX(ID) FROM towed_bike")
	index = cursor.fetchone()[0]
	index = 1 if not index else index + 1
	with open(f'./src/pictures/{index}.jpg', 'wb') as f:
		f.write(res.content)
	
	return path.abspath(f'./src/pictures/{index}.jpg')
	
	
def max_page_index():
	"""return max page index if not page return -1"""
	url = craw_page_url(100)
	res = requests.get(url)
	if(res.status_code != 200):
		with open('./mail.txt', 'a') as f:
			f.write(datetime.now()+"\n")
			f.write(f"can't get data for decide max page!!\n")
			f.write(f"url: {url}\n")
			f.write(f"status code: {res.status_code}\n")
			f.write("\n")
		return

	soup = BeautifulSoup(res.text, 'html.parser')
	if(soup.select("ul.pagination") == []):
		return -1
	index = soup.select("ul.pagination")[0].findChildren(recursive=False)[-2].findChild().findChild().previousSibling.strip()
	return int(index)

def main():
	print(f"program running...")
	print(f"time: {datetime.now()}")

	max_index = max_page_index()

	if max_index == -1:
		print("there is no data to crawl...")
		exit()

	total_add_entry = 0
	for page_index in range(1, max_index+1):
		print(f"\ncrawling {craw_page_url(page_index)}...")
		total_add_entry += get_TowBikes(craw_page_url(page_index))

	print(f"add {total_add_entry} of entry...")

if __name__ == "__main__":
	main()