#!/usr/bin/env python

data = [10,2,3,44,43,23,233,3,22,54,5,10,9,78,34]
count=0
print(len(data))
# for index,i in enumerate(data[0:-1]):
for j in range(1,len(data)):
    for i in range(len(data)-j):
        if data[i]>data[i+1]:
            tmp = data[i+1]
            data[i+1] = data[i]
            data[i] = tmp

    # for index in range(len(data)-1):
    #     if i <index:
    #         if i >data[index+1] :
    #             tmp = data[index+1]
    #             data[index+1] = i
    #             data[index] = tmp
        count += 1
    print(data)
print("count:",count)