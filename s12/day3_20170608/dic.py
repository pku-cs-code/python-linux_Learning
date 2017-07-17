#!/usr/bin/env python

import collections
# dic = {'k1':[]}
# dic['k1'].append('alex')

dic = collections.defaultdict(list)
dic['k1'].append('alex')
print(dic)