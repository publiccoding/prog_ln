class A():
	def __init__(self, arg):
		self.arg = arg


tmp = A.__new__(A)
tmp.__init__("thimma")
a = tmp
print(a.arg)