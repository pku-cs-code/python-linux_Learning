#!/usr/bin/env python

i = 0
name = "zhang"
password = "123"

while i < 3:
    f = open("login.log","r")
    #f.write()
    #f.close()
    block_status = f.read()
    if block_status == "blocked":
        print("sorry, your account is blocked.")
        break
    f.close()
    user_name = input("please input your name:")
    user_pass = input("please input your pass:")
    if user_name == name and user_pass == password:
        print("welcome!\n")
        break
    i += 1
else:
    print("too many retries")
    f = open("login.log","w")
    f.write("blocked")
    f.close()

