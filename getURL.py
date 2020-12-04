import requests
from requests.exceptions import HTTPError, ConnectionError
from datetime import date
import sys
from bs4 import BeautifulSoup
import base64

craw_host_url = "https://mybike.ntu.edu.tw"

base_url = "https://mybike.ntu.edu.tw/bike.announcement/towing" 


# url for web crawling
# this have page 1-?
def crawl_url(_date, page):
	"""get url for the date and page"""
	encode = base64.b64encode(date.strftime(_date, '%Y/%m/%d').encode('utf-8'))
	fdate = '/fdate/' + encode.decode('utf-8')
	page = '/page/' + str(page)

	return base_url + fdate + page


def max_page_index(date):
	"""return max page index if not page return -1(no entry)"""
	url = crawl_url(date, 100)
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
	if(soup.select("ul.pagination") == []):
		return -1
	index = soup.select("ul.pagination")[0].findChildren(recursive=False)[-2].findChild().findChild().previousSibling.strip()
	return int(index)