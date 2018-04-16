import numpy as np
# arr1 = np.array([[1,2,3,4],[1,2,3,4]])
# a = np.arange(1,10,2)
# dt = np.dtype([('age',np.int8)]) 
# a = np.array([(10,),(20,),(30,)], dtype = dt) 
# print(a['age'])

# student = np.dtype([('name','S3'), ('age', 'i1'), ('marks', 'f4')]) 
# a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 

# print(a['name'])

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


x = np.linspace(10,20,5) 
print(x)
# print(x) 
# print(np.logspace(1.0,2.0, num=10))

# print(np.arange(10)[2:])
# print(np.arange(10)[4:8])

# a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
# print(a[0,...])

# x = np.array([[1, 2], [3, 4], [5, 6]]) 
# y = x[[0,2],[1,1]]
# print(y)

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
y = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print(np.concatenate((x,y),axis=1))
print(np.concatenate((x,y),axis=0))
#print(x[1:4,0:2])

