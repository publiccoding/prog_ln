# 1. check pyhton version

# import sys 
# print(sys.version)

# 2. Follow PEP-8 Style Guide 

# 3. Know the diff between bytes,str and Unicode 
# 	Bytes to String (encode('utf-8'))
# 	String to Bytes (decode('utf-8'))
# 4. Write helper function instead of complex expression
# my_values = {'red':	['5','6','7'], 'green':['','9'], 'blue':['0','5']}

# red = my_values.get('red',[''])
# red = red[1] if red[0] else 0
# #red = int(my_values.get('red',[''])[1] or 0)
# green = int(my_values.get('green',[''])[1] or 0)
# opacity = int(my_values.get('opacity',[''])[0] or 0)
# print("Red  %r" % red)
# print("Green %r" % green)
# print("Opacity %r" % opacity)

# 5. how to slice sequence 

# a = [chr(x) for x in range(97, 97+26) ]
# print(a)
# b = [ord(x) for x in a]
# print(b)
# assert a[:5] == a[0:5]

# 6. Avoid Using	start, end, and stride in a Single Slice

# dds = b[::3]
# print(dds)

# 7. Use	List Comprehensions	Instead	of map and filter

# squares = map(lambda x:x ** 2, b)
# even = map(lambda x:x **2, filter(lambda x:x%2==0, b))
# print(even)

# 8. Avoid More Than	Two	Expressions	in List Comprehensions

# matrix=[[1, 2, 3], [4, 5, 6]]
# flat = [[x*x for x in row] for row in matrix ]
# print(flat)

# 9. Generator Expressions for Large Comprehensions

# val = (len(x) for x in open('/home/tim/.bash_logout'))
# print(next(val))
# print(next(val))

# 10. Prefer	enumerate Over range

# flavor_list	=	['vanilla',	'chocolate','pecan','strawberry']
# for i, x in enumerate(flavor_list):
# 	print('%d:%s'%(i,x))

# 11. Use zip to	Process	Iterators in Parallel

# names = ['vanilla',	'chocolate','pecan','strawberry']
# names.append('thimmarayan')
# letters = [len(x) for x in names]
# max_ltr = 0
# long_name = None 

# for x in range(len(name)):
# 	count = len(name[x])
# 	if count > max_ltr:
# 		long_name = name[x]
# 		max_ltr = count
# print(long_name)


# max_ltr = 0
# long_name = None 

# for name, count in zip(names, letters) :
# 	if count > max_ltr:
# 		long_name = name
# 		max_ltr = count
# print(long_name)
# from iterators import zip_longest	 


# names = ['vanilla',	'chocolate','pecan','strawberry']
# letters = [len(x) for x in names]
# names.append('thimmarayan')

# print(names,letters)
# for n, l in zip(names,letters):
# 	print(n,l)

# 12. Avoid else	Blocks After for and while Loops (will not work on no-break)

# The else block	after a loop only runs if the loop body	did	not	encounter a	break statement.
# Avoid using else blocks after loops because their behavior is not intuitive	and	can be confusion
# for i in range(5):
# 	print("Looped %d" % i)
# 	if i > 2:
# 		break
# else:
# 	print("ELSE FOR BLOCK")

# while False:  
# 	print("always runs")
# else: # ( execute else block while fails)
# 	print("while else block")

# 13. Take Advantage of Each Block in try/except/else/finally

try:
	file = open('/home/tim/.profile')
except TypeError as e:
	print(e)
else:
	print("This will print alway")
finally :
	file.close()

