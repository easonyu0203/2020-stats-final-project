
craw_url = "https://mybike.ntu.edu.tw/bike.announcement/towing" 
craw_host_url = "https://mybike.ntu.edu.tw"


# url for web crawling
# this have page 1-?
def craw_page_url(index):
	return craw_url + f'/page/{index}'