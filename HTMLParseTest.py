#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import StringIO, gzip

import urllib, urllib2

import codecs

#http://m.search.naver.com/search.naver?query=


#opener = urllib2.build_opener()
#opener.addheaders = [('User-agent', 'Mozilla/5.0')]
#opener.addheaders=[('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.0 Safari/537.36')]
#opener.urlopen('http://m.search.naver.com/search.naver?query=')

#req = urllib2.Request('http://m.search.naver.com/search.naver?query=')
#req.addheaders=[('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.0 Safari/537.36')]
#r = urllib2.urlopen(req)

#print r.read()




query_args = {'query':'a'}
encoded_args = urllib.urlencode(query_args) 

request = urllib2.Request('http://m.search.naver.com/'+'search.naver')
request.add_header('User-agent', 'Mozilla/5.0')
request.add_header('Accept', 'text/html')
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)


compressedstream = StringIO.StringIO(response.read())
gzipper = gzip.GzipFile(fileobj=compressedstream)

print gzipper.read()


soup = BeautifulSoup(gzipper.read())

#print(soup.prettify())
#print(soup.get_text())

#print soup.find_all('span','rtkx_t')

f = codecs.open("result.txt", 'w', 'utf-8')
#f.write(soup.prettify())
f.write(gzipper.read())
f.close()