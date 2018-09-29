import matplotlib.pyplot as plt
import numpy as np
#用梯度下降法和牛顿法寻找最小值

def Fun(x):#原函数
	return x*np.sin(x)
def PxFun(x):#一次导数
	return np.sin(x)+x*np.cos(x)
def PxxFun(x):#二次导数
	return 2*np.cos(x)-x*np.sin(x)

def GD(x,Left,Right):#梯度下降法
	new_x=x
	step=0.001#梯度下降速度
	Over=False
	time=0#time记录运算次数
	while Over==False:
		new_x=new_x-step*PxFun(x)#作梯度下降
		if Fun(x)-Fun(new_x)<7e-9:#精度
			Over=True
		x=new_x		
		time+=1
	
	return x,time
def newton(x,Left,Right):#牛顿法
	new_x=x
	Over=False
	time=0#time记录运算次数
	while Over==False:
		new_x=new_x-PxFun(x)/PxxFun(x)#作牛顿迭代	
		if abs(Fun(x)-Fun(new_x))<7e-9:#精度
			Over=True
		#if new_x<Left or new_x>Right:
		#	return x		
		x=new_x
		y=Fun(x)
		time+=1
		
	return x,time
def GDTEST(Left,Right):#运行梯度下降法
	i=100
	x_start=Left#从区间起点开始设置出发点
	bestx=[x_start]#初始化最小值的横坐标记录记录
	while x_start<=Right+0.2:
		xx,time=GD(x_start,Left,Right)
		if xx>=Left and xx<=Right:
			if Fun(xx)==i:#找到了与已知记录等值的最小值，附加入最小值记录
				if round(xx,5) not in bestx:
					bestx.append(round(xx,5))
			if Fun(xx)<i:#找到了更小的最小值，直接更新最小值记录
				i=Fun(xx)
				bestx=[round(xx,5)]
			
			print(x_start,xx,bestx,time)#输出本次出发点，本次落脚点，已知最小值，运算次数
		else:
			print(x_start,"超出范围")
		x_start+=0.2#出发点右移0.2再次出发
	return bestx	
def newtonTEST(Left,Right):#运行牛顿法
	i=100
	x_start=Left#从区间起点开始设置出发点
	bestx=[x_start]#初始化最小值的横坐标记录
	while x_start<=Right+0.2:
		xx,time=newton(x_start,Left,Right)
		if xx>=Left and xx<=Right:
			if Fun(xx)==i:#找到了与已知记录等值的最小值，附加入最小值记录
				if round(xx,5) not in bestx:
					bestx.append(round(xx,5))
			if Fun(xx)<i:#找到了更小的最小值，直接更新最小值记录
				i=Fun(xx)
				bestx=[round(xx,5)]
			
			print(x_start,xx,bestx,time)#输出本次出发点，本次落脚点，已知最小值，运算次数
		x_start+=0.2#出发点右移0.2再次出发
	return bestx
	
if __name__ == "__main__":
	Left=-6#定义区间
	Right=8
	print('开始梯度下降法')
	bestx=GDTEST(Left,Right)
	print('使用梯度下降法得到的最小值点：')
	for m in bestx:
		print('x = '+str(m),'y = '+str(Fun(m)))
	
	print()
	print('开始牛顿法')
	bestx=newtonTEST(Left,Right)
	print('使用牛顿法得到的最小值点：')
	for m in bestx:
		print('x = '+str(m),'y = '+str(Fun(m)))






