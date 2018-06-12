from matplotlib import pyplot as plt 
import pandas as pd 
from matplotlib import style
style.use('ggplot')

x=[1,2,3,4,5,6]
y=[2,3,4,5,6,7]
df=pd.DataFrame(x,y)
df2=pd.DataFrame(x,y)
#df.set_index('Data',inplace=True)
print(df.head())
df.plot(label='line one', linewidth=5)
df2.plot(label='line two', linewidth=5)
plt.title('THis is Sample test plot')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.legend()
plt.grid(True,color='K')
plt.show()