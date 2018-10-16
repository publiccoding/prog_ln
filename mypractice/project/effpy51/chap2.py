# 14. Prefer Exceptions to Returning None
# Raise	exceptions to indicate special situations instead of returning None. Expect	thecalling code to handle exceptions properly when they are documented.

# def divid(x,y):
# 	try:
# 		return x / y
# 	except ZeroDivisionError as e:
# 		raise ValueError("Invalid inputs") 

# x, y = 2, 0

# try:
# 	result = divid(x,y)
# except ValueError:
# 	print("invalid inputs")
# else:
# 	print("Result is %1.f"%result)

#15. Know How Closures Interact with Variable Scope

# def addition():
# 	def addval(x):
# 		return 5 + x
# 	return addval

# add =addition()
# print(add(10))
# print(add(15))


def sort_values(values, groups):
	
	def helper(x):
		if x in groups:
			print((0,x))
			return (1,x)
		print((1,x))
		return (0,x)
	values.sort(key=helper)

numbers	=	[8,	3,	1,	2,	5,	4,	7,	6]
group	=	{2,	3,	5,	7}

sort_values(numbers,group)
print(numbers)