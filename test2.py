#-*- coding: utf-8 -*-
import json
import re

j = '''var line1=
[["수, 12 Jun 2013 01:00:00 +0000",22.4916114807,"2 sold"],
["Fri, 14 Jun 2013 01:00:00 +0000",27.4950008392,"2 sold"],
["Sun, 16 Jun 2013 01:00:00 +0000",19.5499992371,"1 sold"],
["Tue, 18 Jun 2013 01:00:00 +0000",17.25,"1 sold"],
["Sun, 23 Jun 2013 01:00:00 +0000",15.5420341492,"2 sold"],
["Thu, 27 Jun 2013 01:00:00 +0000",8.79045295715,"3 sold"],
["Fri, 28 Jun 2013 01:00:00 +0000",10,"1 sold"]];\s*$'''
values = re.findall(r'var.*?=\s*(.*?);', j, re.DOTALL | re.MULTILINE)
for value in values:
    print(json.loads(value))
    print(value)
