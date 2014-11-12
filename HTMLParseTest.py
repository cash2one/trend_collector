#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup


html = urllib.urlopen('http://m.search.naver.com/search.naver?query=')
soup = BeautifulSoup(html)

print(soup.prettify())

print 'ȫȫ  aa'
