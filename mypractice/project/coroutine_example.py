
# def addition():
# 	cur = yield 

# 	while True:
# 		val = yield cur 
# 		cur = val + cur 

# add = addition()

# print(next(add))
# print(add.send(10))
# print(add.send(10))
# print(add.send(10))


def generator_ex(n):
	
	i = 0
	while n > i :
		yield i 
		i +=1
print(type(generator_ex(10)))
for i in generator_ex(10):
	print(i)
