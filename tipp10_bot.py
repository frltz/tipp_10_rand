#!/usr/bin/python

import requests
import sqlite3
import os

for i in (0,1,2):
	page = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary").json()
	res = page['extract'].splitlines()
	title = page['title']
	a = 0

	home = os.path.expanduser('~') + "/.local/share/TIPP10/TIPP10/tipp10v2.db"
	conn = sqlite3.connect(home)

	cursor = conn.execute("select content_lesson+1 from own_content order by content_lesson desc LIMIT 1;")
	for row in cursor:
		pass


	cursor2 = conn.execute("select content_id+1 from own_content order by content_id desc LIMIT 1;")
	for row2 in cursor2:
		pass
	
	cursor3 = conn.execute("select own_id+1 from own_list order by own_id desc LIMIT 1;")
	for row3 in cursor3:
		pass
	
	cursor4 = conn.execute("select own_unit+1 from own_list order by own_unit desc LIMIT 1;")
	for row4 in cursor4:
		pass

	for y in str(len(res)):
		conn.execute("insert into own_content(content_id, content_text, content_lesson) values (?,?,?)",(row2[0], res[int(y)-1],row[0]))
		conn.execute("insert into own_list(own_id, own_name, own_description, own_unit) values (?,?,?,?)", (row3[0], title,a, a))
	conn.commit()
	conn.close()
	
os.system('tipp10')
	
