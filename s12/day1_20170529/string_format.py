#!/usr/bin/env python

name = input("name:").strip("A")
age = input("age:")
job = input("job:").strip()

print("Information of []:" + name +"\nName:[]" + name +"\nAge:[]" + age +"\nJob:[]" + job +"")
msg = '''
Information of %s:
Name:%s
Age:%s
Job:%s
'''%(name,name,age,job)
print(msg)
#print("Information of %s:\nName:%s\nAge:%s\nJob:%s" %(name,name,age,job))
