#使用要求
#要求每个excel文件只有一个sheet，而且格式一样，只有数据不一样
#应用场景是加总很多个相同的excel文件中的数字
#可以根据使用要求自己修改

import os
import pandas as pd
import numpy as np

 
def readname():
    
    #filePath = input('请输入待汇总数据所在的文件夹路径，例如: C:\\Users\\firefly\\Desktop\\数据汇总  \n须保证该文件夹\
#下除待统计的excel文件外，无其它文件或文件夹！ \n文件夹路径:')
    #m = int(input('请输入表格行数：\n'))
    #n = int(input('请输入表格列数：\n'))

    filePath = 'C:\\Users\\firefly\\Desktop\\zhigong'
    names = os.listdir(filePath)
    
    #自动获取表格活动区域行列数
    file=os.path.join(filePath,names[0])
    df = pd.read_excel(file,header=None,keep_default_na=False)
    #行数
    m = df.shape[0]
    #列数
    n = df.shape[1]
    
    print(m,n)
    return names,filePath,m,n


def mergeexcel(m,n,names,filePath):
    
    #创建一个值为0的dataframe用来存数
    pdd=pd.DataFrame(np.zeros([m,n]))
    types=set()
    for name in names:
        #print(pdd)
        file=os.path.join(filePath,name)
        print('正在合并计算'+str(name))
        #读取的时候把NaN值以空值读入，视作无表头
        df = pd.read_excel(file,header=None,keep_default_na=False)
        for i in range(0,m):
            for j in range(0,n):

                #print(pdd)
                # 如果是空值，则跳过        
                if df.iloc[i,j] == '':
                    continue
                # 如果是文字，则原样复制  
                elif type(df.iloc[i,j]) == str:
                    if pdd.iloc[i,j] == 0:
                        pdd.iloc[i,j] = df.iloc[i,j]
                #如果是数字，则继续加总
                elif type(df.iloc[i,j]) == int or float:
                    pdd.iloc[i,j] = pdd.iloc[i,j]+df.iloc[i,j]
                else:
                    print("报错！表格里有数据既不是str也不是int或float,快debug一下！")
  

    return pdd    
 
 
if __name__ == "__main__":
    names,filePath,m,n = readname()
    result = mergeexcel(m,n,names,filePath)
    print(result)
    #指定输出路径，不修改会报错
    with pd.ExcelWriter("C:\\Users\\firefly\\Desktop\\统计结果.xlsx") as writer:
        result.to_excel(writer, sheet_name='result',header=False,index= False)
    print("统计结果已生成！")
    print("请查看: C:\\Users\\firefly\\Desktop\\统计结果.xlsx")
