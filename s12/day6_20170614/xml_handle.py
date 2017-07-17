#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)

"""
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print("------",i.tag,i.attrib,i.text)
"""

#只遍历year节点
"""
for node in root.iter('year'):
    print(node.tag,node.text)
"""

"""
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text =str(new_year)
    node.set("updated","yes")  #设点节点属性为updated="yes"

tree.write("xmltest.xml")
"""
#删除节点

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank >50:
        root.remove(country)

tree.write("xmltest.xml")






# <?xml version="1.0"?>
# <data>
#     <country name="Liechten"></country>
#     <country name="Sigpore">
#         <rank updated="yes">5</rank>  #updated="yes"是属性attrib，5是value，即text，
#         <year>2011</year>
#         <gdppc>59900</gdppc>
#         <neighbour name="Malaysia" direction="N"/>
#     </country>
#     <country name="Panama"></country>
#
# </data>

