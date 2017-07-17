#!/usr/bin/env python

data = [[col for col in range(4)] for row in range(4)]
'''
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
'''
for row in data:
    print(row)
print("-------")
for row_index,row in enumerate(data):
    #print(row_index)
    for col_index in range(row_index,len(row)):
    #if row_index > col_index :
        tmp = data[col_index][row_index]
        data[col_index][row_index] = row[col_index]
        data[row_index][col_index] = tmp
    for r in data:print(r)
    print("--------")
for r in data:print(r)
