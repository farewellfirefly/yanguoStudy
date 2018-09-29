from numpy import *
#python中list和array之间的相互转换以及list和array的遍历
#list存储的是指针


testlist = [[1,2,3],[4,5,6]]
#将list转化成array
testArray = array(testlist)
for i in range(testArray.shape[0]):
	for j in range(testArray.shape[1]):
		print(testArray[i,j],'',end='')
	print()
	
print()
#将array转化成list
toList = testArray.tolist()
for i in range(len(toList)):
	for word in toList[i]:
		print(word,'',end='')
	print()
#list长度为2
