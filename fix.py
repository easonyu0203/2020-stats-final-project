from database import cursor
import base64
from datetime import date, datetime
import concurrent.futures
import requests
from bs4 import BeautifulSoup
from getURL import base_url

def crawl_url(_date, bike_id):
	d_encode = base64.b64encode(date.strftime(_date, '%Y/%m/%d').encode('utf-8'))
	id_encode = base64.b64encode(str(bike_id).encode('utf-8'))
	fdate = '/fdate/' + d_encode.decode('utf-8')
	fpid = '/fpid/' + id_encode.decode('utf-8')

	return base_url + fdate + fpid


def in_web(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	if soup.select("ul.violation-list>li"):
		print(url)
		return True
	else:
		print('not in web')
		return False



cursor.execute("SELECT bike_id, time FROM towed_bike WHERE return_time is not NULL")
urls = []

for bike_id, time in cursor.fetchall():
	urls.append(crawl_url(time, bike_id))
for u in urls:
	in_web(u)

