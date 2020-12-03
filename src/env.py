
craw_url = "https://mybike.ntu.edu.tw/bike.announcement/towing" 
craw_host_url = "https://mybike.ntu.edu.tw"

#content of page 1
last_content = ''

with open('/Users/eason/Desktop/statistics/final-project/src/last_content.txt' , 'r') as f:
	last_content = f.read()


# url for web crawling
# this have page 1-?
def craw_page_url(index):
	return craw_url + '/page'