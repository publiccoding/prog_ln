from collections import Counter
from collections import namedtuple
from collections import deque 

from collections import abc
import pdb
import sys 


City = namedtuple('City', 'name country pop cord')
tokyo = City('Tokyo','JP',36.333, (35.68,145.9))

print(City._fields)    
Latlong = namedtuple('Latlong','lat,long')

delhi_data = City('Delhi','IN',110.5, Latlong(38.90,160.8))

delhi=City._make(delhi_data)
print(delhi)
print(City(*delhi_data))
print(delhi._asdict())

for key, val in delhi._asdict().items():
    print(key, ' ----> ',val)
# lst = ['thimma','rayan','krishna','kumar']

# wc = len(lst)
# cc = 0
# for j in lst:
#     cc += len(j)
# print(wc)
# print(cc)

# dq = deque(range(10),maxlen=8)
# print(dq)
# dq.rotate(4)
# print(dq)
# dq.append((range(3)))
# print(dq)

# my_dict = {}

# print(isinstance(my_dict, abc.Mapping))

nonlat = '字'
print(nonlat)

print(bytes(nonlat, 'utf8'))

