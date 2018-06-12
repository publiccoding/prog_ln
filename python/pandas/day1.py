import pandas as pd 
import numpy as np 

# panda series is immutalbe one dimenstional labled array 

data = np.array([1,2,3,4,5,6])
s=pd.Series(data, index=['a','b','c','d','e','f'])
print(s['c'])

