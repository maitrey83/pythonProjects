import requests
from bs4 import BeautifulSoup

url = "http://www.overstock.com/Home-Garden/1/store.html?TID=TN:FH:FH"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")
prettify = soup.prettify()

linkValue = None
findRels = soup.find_all("link", {"hreflang": "es"})
if findRels != linkValue:
    print(findRels)
