from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("https://baike.baidu.com"+articleUrl)
    bsObj = BeautifulSoup(html, features='lxml')
    return bsObj.find("div",{"class":"content-wrapper"}).find_all("a",{"href":re.compile("^(/item/)((?!:).)*$")})
links = getLinks("/item/Python/407313")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print("https://baike.baidu.com"+newArticle)
    links = getLinks(newArticle)