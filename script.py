import requests
from bs4 import BeautifulSoup

url_dari_target = "https://www.samsung.com/id/"
response = requests.get(url_dari_target)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h2")
print("Title:", title.text)