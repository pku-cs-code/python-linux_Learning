#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pickle
def login(func):
    print("hello")

# f = open("user_acc.txt",'w')
f = open("user_acc.txt",'wb')

info={
    "alex":"123",
    "jack":'4444',
   # "func":login


}

# print(json.dumps(info))
# print(pickle.dumps(info))
pickle.dump(info,f)  #一步解决
# f.write(json.dumps(info))
# f.write(str(info))
#f.write(pickle.dumps(info))

f.close()
