# def greet(name):
#     print("Hello, {0}!".format(name))
# print("What's your name?")
# # name = input()
# # greet(name)

import math

for i in range(10) :
	print(i)
drinks = {
        'martini': {'vodka', 'vermouth'},
        'black russian': {'vodka', 'kahlua'},
        'white russian': {'cream', 'kahlua', 'vodka'},
        'manhattan': {'rye', 'vermouth', 'bitters'},
        'screwdriver': {'orange juice', 'vodka'}
        }
for n, c in drinks.items():
        if 'cream' in c:
        	print(n,c)