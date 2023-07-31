#importing some module
from requests import get
from bs4 import BeautifulSoup as Bs

class GempaNewsClass:
	def __init__(self):
		self.url = "https://www.bmkg.go.id/"

	def getData(self, html):
		soup = Bs(html, 'html.parser')

		#parent elements
		find_news = soup.find('div', class_='gempabumi-home-bg margin-top-13')
		find_info = find_news.find_all('li')

		#store list
		data_list = []

		# get info by index
		get_time = find_info[0].get_text(strip=True)
		get_magnit = find_info[1].get_text(strip=True)
		get_kedalaman = find_info[2].get_text(strip=True)
		get_koordinat = find_info[3].get_text(strip=True)
		get_lokasi = find_info[4].get_text(strip=True)
		get_det_loc = find_info[5].get_text(strip=True)

		# store data into this list on below
		data = {
		'waktu': get_time,
		'magnitude': get_magnit,
		'kedalaman': get_kedalaman,
		'koordinat': get_koordinat,
		'lokasi': get_lokasi,
		'detail': get_det_loc
		}

		data_list.append(data)
		return data_list


	def getNews(self):
		html = get(self.url).content
		data = self.getData(html)
		return data



##Btw this line just for testing that those class work or not
# if __name__ == '__main__':
# 	gempaApp = GempaNewsClass()
# 	html = get(gempaApp.url).text
# 	data = gempaApp.getData(html)

# 	print(data)






