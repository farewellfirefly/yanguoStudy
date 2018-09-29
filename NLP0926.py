import numpy as np

A=np.array([[3,-1,4],[1,0,0],[2,1,-5]])
n=A.shape[0]

E=np.eye(n)
B=np.eye(n)
#定义 mse函数
def MSE(a,b)  :
    if  a.shape!=b.shape:
        return
    mse=0
    for i in range(a.__len__()):
        for j in range(a[0].__len__()):
           mse+=(a[i][j]-b[i][j])**2
    return mse


target=0.000001
alpha=0.001

delta=0.0000001
lmse=999999
ro=0
C=0
mse=MSE(np.dot(A,B),E)
#进入梯度下降循环： 以mse迭代差小于0.000001为目标
while abs(lmse-mse)>target and ro<100000:
    ro+=1
    D=np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            B[i][j]+=delta
            D[i][j]=(MSE(np.dot(A,B),E)-mse)/delta
            B[i][j]-=delta
			
    #加一个动量C获取上一次修改的步长对下一步进行优化
    B=-alpha*D+B+C
    C=-alpha*D*0.9
    
    lmse=mse
    mse=MSE(np.dot(A,B),E)
#简单标注一下当前的批次和结果
    if ro%100==0:
        print(ro)
        print(B)
        print(mse)
        print(np.dot(A,B)-E)
		
    #lmse=mse
for i in range(n):
        for j in range(n):
            B[i][j]=round(B[i][j],3)
print("逆矩阵为")
print(B)
print(ro)
print("a*b:")
print(np.dot(A,B))
