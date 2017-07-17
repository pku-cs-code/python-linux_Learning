#!/usr/bin/env python

# names = iter(['alex','jack','list'])
# print(names)
# print(names.__next__())
# print(names.__next__())
# print(names.__next__())
#print(names.__next__())

# f = open("__init.py")
# f.read()
# f.readlines()
#
# for line in f:
#     print(line)

def cash_out(amount):
  while amount > 0:
    amount -=100
    yield 100
    print("cash out")

atm = cash_out(500)

print(type(atm))
print(atm.__next__())
print(atm.__next__())
print("叫个大保健。。")
print(atm.__next__())
# print(atm.__next__())

