import datetime
import time
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


# def sort_values(values, groups):
	
# 	def helper(x):
# 		if x in groups:
# 			print((0,x))
# 			return (1,x)
# 		print((1,x))
# 		return (0,x)
# 	values.sort(key=helper)

# numbers	=	[8,	3,	1,	2,	5,	4,	7,	6]
# group	=	{2,	3,	5,	7}

# sort_values(numbers,group)
# print(numbers)


#16. Consider Generators Instead of	Returning Lists


# def index_file(handle):
# 	offset = 0
# 	for line in handle:
# 		if line:
# 			print(offset)
# 			yield offset
# 		for word in line:
# 			offset += 1
# 			print(offset)
# 			if word == ' ':
# 				yield offset

# with open('/root/prog_ln/mypractice/project/file1.txt','w') as f:
# 	it= index_file(f)
# 	result = (it, 0, 3)
# 	for val in result:
# 		print(val)

#17. Be	Defensive When Iterating Over Arguments
# Always pass as container to the function 

# def normalize_func(get_iter):
# 	total = sum(get_iter())
# 	result = []

# 	for val in get_iter():
# 		percent = 100 * value/total 
# 		result.appen(percent)
# 	return result


# class ReadVisits(object):
	

# 	def __init__(self, data_path):
# 		self.data_path = data_path

# 	def __iter__(self):
# 		with open(self.data_path) as file:
# 			for line in file:
# 				yield line

# visits = ReadVisits(path)
# percent = normalize_func(visits)
# print(percent)

#18. Reduce	Visual Noise with Variable Positional Arguments

# def log(seq, msg, *val):
# 	if not val:
# 		print('%s: %s'%(seq, msg))
# 	else:
# 		value_str = ', '.join(str(x) for x in val)
# 		print('%s%s%s'%(seq, msg, value_str))

# log(1, 'Favorites', 7, 33)
# log('Favorite numbers',	7, 33)


#19. Provide Optional Behavior with Keyword Arguments

# def	flow_rate(weight_diff, time_diff):
# 	return	weight_diff	/	time_diff
# weight_diff	=	0.5
# time_diff	=	3
# flow = flow_rate(weight_diff, time_diff)
# print('%.3f	kg	per	second' % flow)

#20. Use None and Docstrings to	Specify	Dynamic	Default	Arguments
"""
# Things	to	Remember
# Default arguments	are	only evaluated once  during	function definition	at module load time. This can cause odd behaviors for dynamic values (like {} or []).  
# Use None as the default value	for	keyword	arguments that have	a dynamic value. Document the actual default behavior in the functions	docstring.
"""
def	log(message,	when=None):
	"""Log	a	message	with	a	timestamp.
	Args:
		message: Message to	print.
		when: datetime of when the message occurred.
		Defaults to	the	present	time.
	"""
	when = datetime.date.today() if when is None else when
	print('%s:	%s'	% (message, when))

# log('Hi	there!')
# time.sleep(0.1)
# log('Hi	again!')

#21. Enforce Clarity with Keyword-Only Arguments

# Things	to	Remember
# 	Keyword	arguments make the intention of	a function	call more clear.
# 	Use	keyword-only arguments to force callers to supply keyword arguments for
#   potentially	confusing functions, especially	those that accept multiple Boolean flags.
# 	Python 3 supports explicit syntax	for	keyword-only arguments in functions.
# 	Python 2 can emulate keyword-only arguments for functions by using **kwargs and	manually raising TypeError exceptions.
