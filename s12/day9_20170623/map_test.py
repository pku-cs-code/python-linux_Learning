#!/usr/bin/env python
# -*- coding: utf-8 -*-

li1 = [1,2,3,4]
li2 = [5,6,7,8]
g = lambda x,y:x+y
print list(map(g,li1,li2))