import os 
import shutil


# def filesearch(path):
#     filelist = []
#     destination = r'C:\Users\kristhim\Desktop\thimma\demorepo\shell script'
#     for root,dir, files in os.walk(path):     
#         #print(files)   
#         for file in files:
#             if str(file).endswith('.sh'):
#                 if file not in filelist:
#                     filelist.append(file)
#                     os.rename(os.path.join(root,file),os.path.join(destination,file))
#                 else:
#                     os.remove(os.path.join(root,file))
#     print(filelist)        
    

# if __name__ == '__main__':
#     filesearch(r'C:\Users\kristhim\Downloads')

# def nonmethond(func):
#     def wrapper(*args, **kwargs):
#         print('Decorationr funtion called with arguments')
#         result = func(*args, **kwargs)
#         result =result.upper()
#         print("base function is modified")
#         return result
#     return wrapper

# @nonmethond
# def spark(a,b):
#     return f'{a} {b}'

# a=spark('thimma','rayan')
# print(a)


# class docTest:
#     namespace = 4

#     def __init__(self):
#         self.namespace +=1

# docTest.namespace = 5
# a = docTest()
# b = docTest()
# #a.namespace = 6
# #docTest.namespace = 7 
# print(docTest.namespace)
# print(a.namespace)
# print(b.namespace)
# print(a.__class__.namespace)


# def outfunc(x):
#     def inner(n):
#         return n + x 
#     return inner

# invalue =outfunc(6)
# print(invalue(5))

# class Indenter:
#     def __init__(self):
#         self.level = 0
#     def __enter__(self):
#         self.level +=1
#         return self
#     def __exit__(self,type, value, traceback):
#         self.level -=1
#     def Print(self,text):
#         print( '   ' * self.level + text)

# with Indenter() as indent:
#     indent.Print('Hello')
#     with indent:
#         indent.Print('Thimma')
#         with indent:
#             indent.Print('Rarayan')
#     indent.Print('Good bye')

# from collections import namedtuple
# Car = namedtuple('Car','color milage')
# mycar = Car('red',789)
# print(mycar.color,mycar.milage)

# class Testcar(Car):
#     def hexacar(self):
#         if self.color == 'red':
#             return '#ff000'
#         else :
#             return '000000'

# mytest = Testcar('blue',88797)

# print(mytest.hexacar())
# print(mytest._fields)
# print(mytest._asdict())
# print(mytest._replace(color = 'Blue'))
# print(mytest._make(['white',90808]))

