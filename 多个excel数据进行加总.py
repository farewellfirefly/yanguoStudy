#使用要求
#要求每个excel文件只有一个sheet，而且格式一样，只有数据不一样
#应用场景是加总很多个相同的excel文件中的数字
#可以根据使用要求自己修改

import os
import pandas as pd
import numpy as np

 
def readname():
    
    filePath = input('请输入待汇总数据所在的文件夹路径，例如: C:\\Users\\firefly\\Desktop\\数据汇总  \n须保证该文件夹\
下除待统计的excel文件外，无其它文件或文件夹！ \n文件夹路径:')
    m = int(input('请输入表格区域的行数：\n'))
    n = int(input('请输入表格区域的列数：\n'))
    #获取文件下所有excel文件的名称
    names = os.listdir(filePath)
    return names,filePath,m,n


def mergeexcel(m,n,names,filePath):
    
    #创建一个值全部为0的dataframe用来存数
    pdd=pd.DataFrame(np.zeros([m,n]))
    for name in names:
        #拼接每个excel文件的路径
        file=os.path.join(filePath,name)
        print('正在合并计算'+str(name))
        df = pd.read_excel(file,header=None)
        for i in range(0,m):
            for j in range(0,n):
                #如果是文字，则原样复制
                if type(df.iloc[i,j]) == str:
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
    #指定输出路径，不修改会报错
    with pd.ExcelWriter("C:\\Users\\firefly\\Desktop\\统计结果.xlsx") as writer:
        result.to_excel(writer, sheet_name='result',header=False,index= False)
    print("统计结果已生成！")
    print("请查看: C:\\Users\\firefly\\Desktop\\统计结果.xlsx")
