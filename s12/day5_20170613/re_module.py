#！/usr/bin/env python

import re

'''
re.match("[0-9]")
re.match("[a-zA-Z0-9@._]")
'''

string = "192.168.2.23333"
#m = re.match("[0-9]{3}\.",string)
m=re.match("([0-9]{1,3}\.){3}\d{1,3}",string)
print(m.group())

string2 ="alex \n jack\n tom\n li"
#string2 ="ALEX"
# m = re.search("[\w]",string2)
#大小写不敏感
# m = re.search("[a-z]",string2,flags=re.I)
#m = re.search("^a.*$",string2,flags=re.M)
#$匹配的字符串的结尾，不管是第几行
m = re.search("^a.+[\s]+li+",string2)

print(m.group())
