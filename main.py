from bs4 import BeautifulSoup
import requests
URL = "https://www.apachefriends.org/es/index.html"
for a in BeautifulSoup(requests.get(URL).text, 'html.parser').find('div', {'id': 'download'}).findAll('a'):
    if "Linux".lower() in a.text.lower():
        print(a["href"])
        break
