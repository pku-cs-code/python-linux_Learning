#!/usr/bin/env python
n = 19
guess_count = 0
luck_num = -1
while guess_count <3:
    print("guess num:",guess_count)
    luck_num = int(input("please input your luck num:"))
    if luck_num > n:
        print("The num you input is large.")
    elif luck_num < n:
        print("The num you input is small")
    else:
        print("bingo!")
        break
    guess_count += 1
else:
   print("too many retries..")
# if luck_num == n:
#     print("bingo")
# else:
#     print("too many retries..")