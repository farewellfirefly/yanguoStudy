#查找list中出现次数最多的元素
def top(list):
	s = set(list)
	d = {}
	for i in s:
		d[i]=list.count(i)
	print('下面输出的是前k个字典：',end = '')
	print(d)
	list1 = []
	for i in d.values():
		list1.append(i)
		
	ma = max(list1)
	key_max = get_keys(d,ma)
	string = key_max[0]
	return string

#get_keys实现已知dict的value返回key
def get_keys(d,value):
	return [k for k,v in d.items() if v==value]
	
if __name__=='__main__':
	listTest = [1,1,1,2,2,3,4,5,5,6,6,6,6,6,7]
	s = top(listTest)
	print('出现次数最多的元素 ',s)