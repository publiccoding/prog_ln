
class Calculator(object):
	
	def add(self,x,y):
		return x + y

if __name__ == "__main__":
	calc = Calculator()
	result = calc.add(4,5)
	print(result)

	