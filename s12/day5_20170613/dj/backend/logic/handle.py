#!/usr/bin/env python

from backend.db.sql_api import select



def home():
    print("welcome to homepage")
    q_data = select("user",'ddd')
    print("query res:",q_data)
def movie():
    print("welcome to movie page")

def tv():
    print("welcome to tv page")

