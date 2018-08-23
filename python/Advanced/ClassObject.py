class A:
	def __init__(self, arg):
		self.arg = arg
		print("this is example")


tmp=A.__new__(A,'an args')
print(type(tmp))
print("tmp")
tmp.__init__('an arg')
a = tmp
print(type(a))
print(a.arg)
