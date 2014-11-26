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


IssueObj 	  = ''   #실시간 이슈
SisaIssueObj  = ''   # 뉴스
EnterNewsObj  = ''   # 연예
SportsNewsObj = ''   # 스포츠

# Site Data 긁어 오기
def getHTMLData():
	request = urllib2.Request('http://m.search.daum.net/'+'search?q=')
	#request = urllib2.Request('http://m.search.naver.com/'+'search.naver')
	request.add_header('User-agent', 'Mozilla/5.0')
	request.add_header('Accept', 'text/html')
	request.add_header('Accept-encoding', 'gzip')
	response = urllib2.urlopen(request)

	compressedstream = StringIO.StringIO(response.read())
	gzipper = gzip.GzipFile(fileobj=compressedstream)

	return gzipper.read()


# HTML JavaScript var Parsing
def javascriptParsing(str, HTML):
	return re.findall(r'var '+str+'.*?=\s*(.*?);', HTML, re.DOTALL | re.MULTILINE) [0]


# Make Corrent JSON Structure
def makeJSONStructure(data):
	data = re.sub(r'keyword:',' "keyword":',data)
	data = re.sub(r'type:',' "type":',data)
	data = re.sub(r'value:',' "value":',data)

	return data


# Get JSON data
def getData(str, HTMLStr):
	data = javascriptParsing(str, HTMLStr)
	data = makeJSONStructure(data)
	data = json.loads(data)

	return data


HTMLStr = getHTMLData()


IssueObj = getData('IssueObj', HTMLStr)
SisaIssueObj = getData('SisaIssueObj', HTMLStr)
EnterNewsObj = getData('EnterNewsObj', HTMLStr)
SportsNewsObj = getData('SportsNewsObj', HTMLStr)


for i in IssueObj:
	print i['keyword']+' '+i['type']+' '+i['value']

for i in SisaIssueObj:
	print i['keyword']+' '+i['type']+' '+i['value']

for i in EnterNewsObj:
	print i['keyword']+' '+i['type']+' '+i['value']

for i in SportsNewsObj:
	print i['keyword']+' '+i['type']+' '+i['value']


