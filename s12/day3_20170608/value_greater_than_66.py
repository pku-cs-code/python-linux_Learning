#!/usr/bin/env python

from collections import defaultdict
values = [11,22,33,44,55,66,77,88,99,90]
my_dict = defaultdict(list)
my_dict = {}
for value in values:
    if value>66:
        my_dict['k1'].append('value')
    else:
        my_dict['k2'].append['value']
