#!/usr/bin/python3

# class Test:
   
#     def __call__(self,*args,**kwargs):
#         print(args,kwargs)

# t = Test()
# t(1,2,3,4, thimma="krish")

# class Test2:
#     def __init__(self):
#         pass

#     def calling(self):
#         return 42
#     def called(self):
#         return self.calling()

# print(Test2().called())

import sys

t='thimma'.capitalize

print(sys.platform)
print(2**200)
print('Spam!'*8)
#input()

val = ['thimma','rayan','krishnappa','varaganappalli']

def capital(x):
    for v in x:
        return v.capitalize()
def upper_(x):
    for v in x:
        return v.upper()

print([ x.capitalize() for l in val if len(val) >2 for x in l.upper() if len(l) > 5 ])

