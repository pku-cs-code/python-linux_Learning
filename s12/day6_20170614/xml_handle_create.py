#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
age.text ='33'
sex.text= 'Male'

name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age2 = ET.SubElement(name2,"name",attrib={"checked":"no"})
sex2 = ET.SubElement(name2,"sex")
age.text = '24'
sex2.text ='Female'

et =ET.ElementTree(new_xml)
et.write("test_new.xml",encoding="utf-8",xml_declaration=True)

ET.dump(new_xml) #打印生成的格式


