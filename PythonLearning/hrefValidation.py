import requests
from bs4 import BeautifulSoup

url = "http://www.overstock.com/Home-Garden/Furniture/32/dept.html"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")
prettify = soup.prettify()
# linkPosition = [0,1]

linkValue = None
findRels = soup.find_all("link", {"hreflang": "es"})
if findRels != linkValue:
    print(findRels)
