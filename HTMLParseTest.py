#-*- coding: utf-8 -*-

import StringIO, gzip

import re

import urllib, urllib2

import json


# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


#http://m.search.naver.com/search.naver?query=
#http://m.search.daum.net/search?q=



query_args = {'query':'a'}
encoded_args = urllib.urlencode(query_args) 

#request = urllib2.Request('http://m.search.naver.com/'+'search.naver')
request = urllib2.Request('http://m.search.daum.net/'+'search?q=')
request.add_header('User-agent', 'Mozilla/5.0')
request.add_header('Accept', 'text/html')
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)


compressedstream = StringIO.StringIO(response.read())
gzipper = gzip.GzipFile(fileobj=compressedstream)

#print gzipper.read()



str = gzipper.read()

values = re.findall(r'var IssueObj.*?=\s*(.*?);', str, re.DOTALL | re.MULTILINE)

print '실시간이슈'
print values[0]

data = values[0]

data = re.sub(r'keyword:',' "keyword":',data)
data = re.sub(r'type:',' "type":',data)
data = re.sub(r'value:',' "value":',data)

print data

data = json.loads(data)


for i in data:
	print i['keyword']+' '+i['type']+' '+i['value']



# values = re.findall(r'var SisaIssueObj.*?=\s*(.*?);', str, re.DOTALL | re.MULTILINE)

# print '뉴스'
# print values[0]



# values = re.findall(r'var EnterNewsObj.*?=\s*(.*?);', str, re.DOTALL | re.MULTILINE)

# print '연예'
# print values[0]




# values = re.findall(r'var SportsNewsObj.*?=\s*(.*?);', str, re.DOTALL | re.MULTILINE)

# print '스포츠'
# print values[0]