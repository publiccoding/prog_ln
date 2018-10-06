# pylint example 
#pylint --reports=n --disable=deprecated-module simplecaeser.py
#pylint --reports=n --disable=deprecated-module --const-rgx='[a-z_][a-z0-9_]{2,30}$'  simplecaeser.py

#from module.maths_operation import mathsTest
# a=[]
# def myTest(a):
#     """
#     >>> myTest(a=[])
#     list
#     """
#     return list 

#doctest: +REPORT_NDIFF
# def multiply(a, b):
#     """
#     >>> multiply(4, 3)   
#     12
#     >>> multiply('a', 3) #doctest: +NORMALIZE_WHITESPACE
#     'aaa' 
#     """
#     return a * b

# class MyClass:
#     pass

# def unpredictable(obj):
#     """Returns a new list containing obj.

#     >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
#     [<doc_test.MyClass object at 0x...>]
#     """
#     return [obj]

# def foo():
#     """
#     >>> foo()
#     hello ...
#     """
#     print("hello world")

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)

# class MyClass:
#     pass 
# def unpredictable(obj):
#     """ retunrs new list containing obj.
#     >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
#     [<doc_test.MyClass object at 0x...>]
#     """
#     return [obj]
    
# def double_space(lines):
#     """Prints a list of lines double-spaced.

#     >>> double_space(['Line one.', 'Line two.'])
#     Line one.
#     <BLANKLINE>
#     Line two.
#     <BLANKLINE>
#     """
#     for l in lines:
#         print(l)
#         print()

def doctest_list(a):
    """
    >>> doctest_list(5)
    [0, 1, 4, 9, 16]
    """
    l = [x*x for x in range(a)]
    return l 



        