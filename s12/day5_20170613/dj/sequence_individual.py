#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import json
def login():
    print("welcome")

f = open("user_acc.txt","rb")
# f = open("user_acc.txt","rb")

#data_from_atm  = f.read()


# data_from_atm = json.loads(f.read())
# data_from_atm = pickle.loads(f.read())
data_from_atm = pickle.load(f)

data_from_atm['func']()
# for i in data_from_atm:
#     print(i)
print(data_from_atm)
