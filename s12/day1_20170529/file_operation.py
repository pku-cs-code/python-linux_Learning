#!/usr/bin/env python2

'''f = open("test.log","w")

f.write("This is the first line\n")
f.write("This is the 2nd line\n")
f.write("This is the 3rd line\n")
f.write("This is the 4th line\n")
'''
f = open("test.log","w+")
f.write("new line\n")
#print ("%s",% f.read())
f.close()