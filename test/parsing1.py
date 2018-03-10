# import cProfile

# def add(x,y):

#     return x + y

# def mul(x,y):
#     return x * y

# def div(x,y):
#     return x / y

# def main(x,y):
#     print(add(x,y))
#     print(mul(x,y))
#     print(div(x,y))
# if __name__ == '__main__':

#    main(2,3)

# def my_func(a,b):
#     """
#     >>> my_func(3,4)
#     12
#     >>> my_func(3,5)
#     20
#     """
#     return a * b

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

from zipfile import ZipFile
import os

# path = 'C:\\Users\\kristhim\\Desktop\\thimma\\demorepo\\shellscript'

# with ZipFile('C:\\Users\\kristhim\\Desktop\\thimma\\demorepo\\shellscript.zip','w') as zip:
#     for root,dir,files in os.walk(path):
#         for file in files:
#             filepath=os.path.join(root,file)
#             zip.write(filepath)

zipobject = ZipFile('C:/Users/kristhim/Desktop/thimma/demorepo/shellscript.zip')
# for name in zipobject.namelist():
#     print(zipobject.getinfo(name))

from collections import OrderedDict, defaultdict,ChainMap
from types import MappingProxyType

# d = OrderedDict(one=1,two=2)
# d['four']=4
# del d['two']
# d['two']=2
# print(d)


# dd = defaultdict(list)
# dd['dog'].append('thimma')
# dd['dog'].append('rayana')
# dd['dog'].append('krishnappa')
# print(dd['dog'])

# dict1={'name':'thimma','age':29,'addr':'varaganappali'}
# dict2={'dept':'software','location':'Bangalore'}
# cmap = ChainMap(dict1,dict2)
# print(cmap['location'])

# write = {'one':1,'two':2,'three':3,}
# print(write)
# rdict = MappingProxyType(write)
# print(rdict)
# rdict['three']=45
# write['three']=45
# print(write)


#list :

# arr =['one','two','three']
# arr[1]='thimma'
# print(arr[1])
# del arr[1]
# print(arr[1])

# tup=('one','two','three')
# print(tup)

from array import array

arr = array('f',(4.5,5.6,2.1,3.4))
arr.append(43)
print(arr)
#arr[2]='thimma'
arr ='abcdefgh'
print(arr[1])
print(arr)
alist=list(arr)
print(alist)
print(''.join(alist))


barr = bytes((0,1,2,3,4))
print(barr)
#barr[2]=23

#del barr[1]
print(barr)

byte = bytearray((0,1,2,3,4,5))
print(byte)
byte[1]=45

print(byte[1])
del byte[2]
byte.append(45)
print(byte)


# car1 ={
#     'color':'red',
#     'milage':7799.9,
#     'automatic':True,
# }

# car2 ={
#     'color':'Blue',
#     'milage':8989.9,
#     'automatic':False,
# }
# car1['milage']=45
# car1['windshield']='closed'
# print(car1)

car1 = ('red','milage',True)
print(car1[1])
print(car1)
print(car1[2])

class Car:
    def __init__(self,color,milage,automatic):
        self.color = color
        self.milage = milage
        self.automatic = automatic
    
car = Car('red',5432.1,True)
car1 = Car('red',5432.1,True)
print(car.color)
car1.windshield='Closed'
print(car1.windshield)
print(car1)

from typing import NamedTuple
from types import SimpleNamespace
class Car(NamedTuple):
    color:int 
    milage:int
    automatic:bool

cars = Car('red',7879.099,'thimma')
print(cars)

carv = SimpleNamespace(color='red',milage=7897.9,automatic=True)
carv.windshield='Closed'
print(carv)

vowels ={'a','e','i','o','u'}
if 'a' in vowels:
    print('Value found')

vowels.add('p')
print(vowels)

fs = frozenset(vowels)
print(fs)

import collections
count = collections.Counter()
inv = {'sword':2,'red':1,'loop':0}
count.update(inv)
print(count)
inv_r = {'red':1,'value':1,'sword':1}
count.update(inv_r)
print(count)

# Stack implementation 

a = []
a.append('eat')
a.append('seat')
a.append('value')

print(a)
print(a.pop())
print(a.pop())
print(a.pop())

from collections import deque

d = deque()
d.append('eat')
d.append('seat')
d.append('value')
print(d)
print(d.pop())
print(d.pop())
print(d.pop())

from queue import LifoQueue

lq = LifoQueue()
lq.put('eat')
lq.put('seat')
lq.put('value')
print(lq)
print(lq.get())
print(lq.get())
print(lq.get())

#FIFO using list

fifo = []
fifo.append('eat')
fifo.append('seat')
fifo.append('value')

print(fifo)
print(fifo.pop(0))
print(fifo.pop(0))
print(fifo.pop(0))
print(fifo)


#FIFO using deque

fd = deque()
fd.append('eat')
fd.append('seat')
fd.append('value')
print(fd)
print(fd.popleft())
print(fd.popleft())
print(fd.popleft())
print(fd)

#queue 
from queue import Queue
qu = Queue()
qu.put('eat')
qu.put('seat')
qu.put('value')
print(qu)
print(qu.get())
print(qu.get())
print(qu.get())


# multiprocessing queue 

from multiprocessing import Queue

mq = Queue()
mq.put('eat')
mq.put('seat')
mq.put('value')
print(mq)

print(mq.get())
print(mq.get())
print(mq.get())
#print(mq.get())


#Priority Queue

pq = []
pq.append((2,'two'))
pq.append((1,'one'))
pq.append((3,'three'))
print(pq)
pq.sort(reverse=True)
while pq :
    print(pq.pop())

#Priority Queue heapq 

import heapq

ph = []

heapq.heappush(ph,(2,'two'))
heapq.heappush(ph,(1,'one'))
heapq.heappush(ph,(3,'three'))

while ph:
    print(heapq.heappop(ph))

from queue import PriorityQueue
pri = PriorityQueue()
pri.put((2,'two'))
pri.put((1,'one'))
pri.put((3,'three'))
print(pri)

while not pri.empty():
    print(pri.get())

my_item = ['a','b','c']

for i in my_item:
    print(i)

i =0
while i < len(my_item):
    print(my_item[i])
    i +=1

for i , item in enumerate(my_item):
    print(i, item)

class Iterator:
    def __init__(self,value, maxlen):
        self.value = value
        self.maxlen = maxlen
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.maxlen:
            raise StopIteration
        self.count +=1
        return self.value

iter = Iterator('Hello Thimma',3)

for i in iter:
    print(i)

def Repeater(cha, val):
    for _ in range(val):
        yield cha 

rep = Repeater('thimma',3)

for item in rep:
    print(item)