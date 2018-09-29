#0927——王彦国——NLP作业
import matplotlib.pyplot as plt
import numpy as np
 
def Fun(x):#原函数
	return x*np.sin(x)
 
def PxFun(x):#求导数,为了方便这里直接手算，没有用算法求导
	return np.sin(x)+x*np.cos(x)
 
def solve(x)
	#初始化
	fig=plt.figure()#figure对象
	x=np.arange(-6,8,0.001)
	y=Fun(x)
	plt.plot(x,y)
	 
	#梯度下降
	step=0.001#下降系数
	x=-6
	y=Fun(-6)#初始选取一个点
	tag_x=[x]
	tag_y=[Fun(x)]#两个坐标分别打入表中，该表用于绘制点
	new_x=x
	new_y=y
	Over=False
	time=0

	while Over==False:
		new_x=new_x-step*PxFun(x)#作梯度下降
		
		if Fun(x)-Fun(new_x)<7e-9:#精度
			Over=True
		x=new_x
		y=Fun(x)
		time+=1
		if time%50 == 0:
			tag_x.append(x)
			tag_y.append(Fun(x))#每迭代五十次，新点坐标打入表中    
	 
	#绘制点/输出坐标
	plt.plot(tag_x,tag_y,'r*')#将逼近的过程打点绘制
	plt.title('(x,y)~('+str(x)+","+str(y)+')')
	plt.show()
