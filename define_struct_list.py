#通过下面这种方式自定义结构化数组
import numpy as np
import pandas as pd
dtypes={'name':'s32','age':'i','weight':'f'}
mydata=pd.DataFrame([['zhang',32,65.5],['wang',24,55.2]],columns=['name','age','weight'])
print(mydata)
t=np.shape(mydata)
print(t)
for i in mydata.columns:
	print('')
	for j in range(mydata.ndim):
		print(''+str(mydata[i][j]),'',end='')
		
list1 = [1,2,3]
list2 = (1,2,3)
array1 =np.array([[4,5,6],[1,2,3]])
print(list1)
print(np.shape(array1))
print(array1[1:])
print(type(list1))
print(type(list2))
print(type(array1))

