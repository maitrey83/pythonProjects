import logging

import requests
from bs4 import BeautifulSoup

# import urllib2
logging.basicConfig(filename='scrapingLogs.log', level=logging.INFO)
url = "http://www.overstock.com/Home-Garden/Furniture/32/dept.html"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")
prettify = soup.prettify()
findLinks = soup.find_all("div", {"id": "brd-crumbs"})
# print(findLinks)

for hrefLinks in findLinks:
    try:
        firstBreadCrumb = hrefLinks.contents[1].find_all("li", {"typeof": "v:Breadcrumb"})[0].text
        secondBreadCrumb = hrefLinks.contents[1].find_all("li", {"typeof": "v:Breadcrumb"})[1].text
        breadCrumb = hrefLinks.contents[1].find_all("li", {"class": "bcrumb-3 last-refinement"})[0].text
        logging.info("Breadcrumbs are displaying")
    except:
        pass
