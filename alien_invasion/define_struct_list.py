#通过下面这种方式自定义结构化数组
from numpy import *
import pandas as pd
dtypes={'name':'s32','age':'i','weight':'f'}
mydata=pd.DataFrame([['zhang',32,65.5],['wang',24,55.2]],columns=['name','age','weight'])
print(mydata)
t=mydata.shape
for i in mydata.columns:
	print('')
	for j in range(mydata.ndim):
		print(''+str(mydata[i][j]),end='')