#-*- coding: utf-8 -*-

import StringIO, gzip

import re

import urllib, urllib2

import json

import MySQLmodule as mdb


#http://m.search.naver.com/search.naver?query=
#http://m.search.daum.net/search?q=


IssueObj 	  = ''   #실시간 이슈
SisaIssueObj  = ''   # 뉴스
EnterNewsObj  = ''   # 연예
SportsNewsObj = ''   # 스포츠

ymd  = ''
time = ''

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

	data = re.sub(r'"new"','"="',data)

	return data


# Get JSON data
def getData(str, HTMLStr):
	data = javascriptParsing(str, HTMLStr)
	data = makeJSONStructure(data)
	data = json.loads(data)

	return data


# Add JSON element
def addData(key, data, json):
	for i in range(0, len(json)):
		json[i][key] = data

	return json


# get HTML document
HTMLStr = getHTMLData()


# get JSON data each search category
IssueObj = getData('IssueObj', HTMLStr)
SisaIssueObj = getData('SisaIssueObj', HTMLStr)
EnterNewsObj = getData('EnterNewsObj', HTMLStr)
SportsNewsObj = getData('SportsNewsObj', HTMLStr)


# 사이트, 검색 종류 json에 추가
IssueObj = addData('site_se', '1', IssueObj)
IssueObj = addData('search_se', '1', IssueObj)

SisaIssueObj = addData('site_se', '1', SisaIssueObj)
SisaIssueObj = addData('search_se', '2', SisaIssueObj)

EnterNewsObj = addData('site_se', '1', EnterNewsObj)
EnterNewsObj = addData('search_se', '3', EnterNewsObj)

SportsNewsObj = addData('site_se', '1', SportsNewsObj)
SportsNewsObj = addData('search_se', '4', SportsNewsObj)



# 실시간 검색 일자 파싱
data = javascriptParsing('issueTime', HTMLStr)

data = re.sub(r'[\'\.\:]', '', data)

data = data.split()

ymd  = '2014' + data[0]
time = data[1]


# Insert into DB
mdb.insertJSONwithDate(IssueObj, ymd, time)
mdb.insertJSONwithDate(SisaIssueObj, ymd, time)
mdb.insertJSONwithDate(EnterNewsObj, ymd, time)
mdb.insertJSONwithDate(SportsNewsObj, ymd, time)