#!/usr/bin/env python
n = 19
luck_num = -1
while luck_num != n:
    luck_num = int(input("please input your luck num:"))
    if luck_num > n:
        print("The num you input is large.")
    elif luck_num < n:
        print("The num you input is small")
print("bingo")
