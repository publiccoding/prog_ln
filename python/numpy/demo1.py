import numpy as np
# arr1 = np.array([[1,2,3,4],[1,2,3,4]])
# # a = np.arange(1,10,2)
# dt = np.dtype([('age',np.int8)]) 
# a = np.array([10,20,30], dtype = dt) 
# print(a['age'][0])

# student = np.dtype([('name','S3'), ('age', 'i1'), ('marks', 'f4')]) 
# a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 

# print(a['name'])
# print(a['age'])
# print(arr1.shape)
# print(arr1.reshape(4,2))
# print(arr1.itemsize)

# print(arr1.itemsize)
# print(arr1.size)

# item_size = (arr1.ndim * arr1.itemsize)
# print(item_size)

# x = np.empty([3,1], dtype = int) 
# print(x)
# print (x.shape)
# print (x.ndim)

# print(np.zeros((6,2),dtype=np.int))
# print(np.ones((6,2),dtype=np.int))

# print(np.asarray((1,2,4)))
# list = range(5) 
# it = iter(list)  

# # use iterator to create ndarray 
# x = np.fromiter(it, dtype = float) 
# print(x)

# print(np.arange(2,30,5))
# print(np.random.random(3))


x = np.linspace(10,20,5) # evenly distributed data 
print(x)
print(x) 
print(np.logspace(1.0,2.0, num=10))

# print(np.arange(10)[2:])
# print(np.arange(10)[4:8])

# a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
# print(a[0,...])

# x = np.array([[1, 2], [3, 4], [5, 6]]) 
# y = x[[0,2],[1,1]]
# print(y)

# x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
# y = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

# print(np.concatenate((x,y),axis=1))
# print(np.concatenate((x,y),axis=0))
# #print(x[1:4,0:2])


# class Car:
#     def __init__(self,name=None,owner=None):
#         self.name = name
#         self.owner = owner 
        
#     def __nonzero__(self):
#         print(self.name)
        
#         return (bool(self.name))

# c1 = Car()
# c2 = Car('audi','thimma')
# c3 = Car()
# if c1:
#     print("C1 has value")
# if c2:
#     print("C2 has value")
# if c3:
#     print("C3 has value")

# class StaffIterator:
    
#     def __init__(self,iterable):
#         self.iterable = iterable
#         self.i=0
    
#     def next(self):
#         if len(self.iterable.members) <= self.i: raise StopIteration
#         v = self.iterable.members[self.i]
#         self.i +=1
#         return v

# class Staff:
#     def __init__(self,company="ABC Inc"):
#         self.company= company
#         self.members = []
#     def employ(self, member):
#         self.members.append(member)
#         print(member,"Employed")
#     def list_(self):
#         print("Employee List is ")
#         for member in self.members: print(member, end=' ')
#     def __iter__(self):
#         return StaffIterator(self)

# s = Staff("EMC Corporation")
# s.employ("thimma")
# s.employ("lakshmi")
# s.employ("Kumar")
# for i in s: 
#     print(i)


# class myiter:
    
#     def __init__(self,member):
#         self.member = member
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         return self.member
    
    
# myit = myiter("thimma")

# print(type(myit))
# for i in myit:
#     print(i)