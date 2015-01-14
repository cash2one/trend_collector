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





def insertDMTrend(ymd):
	con = mdb.connect(host='localhost', user='trend', passwd='trend', db='trend', use_unicode = 'True', charset = 'utf8');

	with con:
		cur = con.cursor()

		cur.execute(" \
				DELETE FROM DM_TREND \
				WHERE SEARCH_DATE = " + ymd + " \
			")

		cur.execute(" \
				INSERT INTO DM_TREND (SITE_SE, SEARCH_SE, SEARCH_DATE, SUM_RANK, KEYWORD, AVG_RANK, COUNT) \
				SELECT 	'1' \
					,	SEARCH_SE \
					,	SEARCH_DATE \
					,	SUM(RANK_VALUE) AS SUM_RANK \
					,	KEYWORD \
					,	ROUND(AVG(RANK),1) AS AVG_RANK \
					,	COUNT(*)  AS COUNT \
				FROM	( \
					SELECT	SEARCH_SE \
						,	SEARCH_DATE \
						,	CASE WHEN RANK = 1 THEN 10 \
								 WHEN RANK = 2 THEN 9 \
								 WHEN RANK = 3 THEN 8 \
								 WHEN RANK = 4 THEN 7 \
								 WHEN RANK = 5 THEN 6 \
								 WHEN RANK = 6 THEN 5 \
								 WHEN RANK = 7 THEN 4 \
								 WHEN RANK = 8 THEN 3 \
								 WHEN RANK = 9 THEN 2 \
								 WHEN RANK = 10 THEN 1 \
							END AS RANK_VALUE \
						,	KEYWORD \
						,	RANK \
					FROM 	REAL_SEARCH_WORD \
					WHERE	SEARCH_DATE = '" + ymd + "' \
					) T1 \
				GROUP BY SEARCH_SE, SEARCH_DATE, KEYWORD \
			")
		cur.execute("commit")