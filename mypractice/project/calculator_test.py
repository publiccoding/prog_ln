import unittest
from calculator import Calculator 

class TestCalculator(unittest.TestCase):
	

	def setUp(self):
		self.calc = Calculator()

		self.dic = {"name":"thimmarayan","age":30}	
		self.dict = {"name":"thimmarayan","age":30}	
		self.l1 = [1,2,3]
		self.l2 = [3,2,1]
	
	# def test_add_method(self):
	# 	self.assertEqual('helloworld',self.calc.add('hello','world'))
	
	
	# def test_bool_true(self):
	# 	self.assertTrue(1)

	
	# def test_bool_true(self):
	# 	self.assertFalse(0)

	
	def  test_assert_raise(self):
		self.assertRaises(TypeError,self.calc.add, "Hello")
	# 	with self.assertRaises(AttributeError):
	# 		[].get()
	

	def test_dict(self):
		self.assertDictEqual(self.dic,self.dict) 


	# def test_list_count(self):
	# 	self.assertListEqual(self.l1,self.l2)


	def test_list_equal(self):
		self.assertItemsEqual(self.l1,self.l2)

		
	def test_add_method(self):
		self.assertAlmostEqual(1,1.2,delta=0.2)
	
	
	def test_add_method(self):
		self.assertAlmostEqual(1,1.000002,places=5)

	
	def test_identical(self):
		self.assertIs("a","a")
	
	
	def test_instances(self):
		self.assertIsInstance(self.calc, Calculator)
	

	def test_not_instance(self):
		self.assertNotIsInstance(1,str)

	
	def test_none(self):
		self.assertIsNone(None)


	def test_assert_raises(self):
		self.assertRaises(IndexError, [1,2,3].pop, 3)

#!/usr/bin/env 
if __name__ == '__main__':
	unittest.main()
