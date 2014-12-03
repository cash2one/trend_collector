#-*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import json




# try:
#     con = mdb.connect('localhost', 'trend', 'trend', 'trend');

#     cur = con.cursor()
#     cur.execute("INSERT INTO trend.TEST VALUES ('B')")
#     cur.execute("commit")

#     #ver = cur.fetchone()
#     #print "Database version : %s " % ver
    
# except mdb.Error, e:
  
#     print "Error %d: %s" % (e.args[0],e.args[1])
#     sys.exit(1)
    
# finally:    
        
#     if con:    
#         con.close()




def insertJSONwithDate(json, ymd, time):
	con = mdb.connect(host='localhost', user='trend', passwd='trend', db='trend', use_unicode = 'True', charset = 'utf8');

	with con:
		cur = con.cursor()

		i = 0;

		for data in json:
			i += 1
			cur.execute(" \
				INSERT INTO trend.REAL_SEARCH_WORD \
					(SITE_SE, SEARCH_SE, SEARCH_DATE, SEARCH_TIME, RANK, KEYWORD, RANK_TYPE, RANK_VALUE) \
				VALUES ('" + data['site_se'] + "', '" + data['search_se'] + "', '" + ymd + "', '" + time + "', " 
				      + str(i) + ", '" + data['keyword'] + "', '" + data['type'] + "', '" + data['value'] + "' ) \
					")
			cur.execute("commit")
