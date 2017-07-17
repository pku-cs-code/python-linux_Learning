#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import zipfile

shutil.make_archive("D:\\test","zip",root_dir="D:\\test")

z = zipfile.ZipFile('D:\\test3.zip','w')
z.write('D:\\test')
z.write('D:\\test2\\test1.txt')
z.close()
