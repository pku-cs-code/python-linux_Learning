#!/usr/bin/env python

import re

#m = re.match("abc","abcdef")
#match是从开头匹配
# m = re.match("[0-9][0-9]","755ab6cdef")
#m = re.match("[0-9]{0,10}","754545454543335ab6cde0f")
#m = re.match("[0-9]{10}","754545454543335ab6cde0f")

#m = re.findall("[0-9]{0,10}","754545454543335ab6cde0f")

#m = re.findall("[0-9]{1,10}","754545454543335ab6cde0f")
m = re.findall("[a-zA-Z]{1,10}","754545454543335ab6cde0Zf")
m = re.findall(".*","754545454543335ab6cde0Zf")
m = re.findall(".+","7545454545433@~_35ab6cde0Zf")
m = re.findall("\S","7545454545433@~_35ab6 cde0Zf")
#匹配一个或者多个加+
m = re.findall("[a-zA-Z]+","7545454545433@~_35ab6 cde0Zf")
m = re.search("\d+","754545.4545433@~_35ab6 cde0Zf")
m = re.search("\d+","sd754545.4545433@~_35ab6 cde0Zf")
#sub替换
m = re.sub("\d+","|","sd754545.4545433@~_35ab6 cde0Zf")
m = re.sub("\d+","|","sd754545.4545433@~_35ab6 cde0Zf",count=2)
m = re.search("^\d+","sd754545.4545433@~_35ab6 cde0Zf")
m = re.search("^\d+$","sd754545.4545433@~_35ab6 cde0Zf1")
#数字中间不能有字母，连续匹配
m = re.search("^\d+$","2121d2133")

#m = re.findall(".","754545454543335ab6cde0Zf")

if m:
    #print(m)
    print(m.group())

