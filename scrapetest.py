from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.text
    except AttributeError as e:
        return None
    return title

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
title = getTitle(url)
if getTitle == None:
    print('Title not found!')
else:
    print(title)