import os

#使用os模块，把文件夹中的所有文件重命名。
#例如，当前test目录下所有的文件名开头添加new_这个字符串。
'''lis=[]
lis.append(os.listdir())

for x in range(len(lis)):
    print(len(lis))#这里lis的长度只有1
'''

#print(type(os.listdir())) os.listdir是一个list类型

for x in range(len(os.listdir())):
    
    text="new_"+os.listdir()[x]
    os.rename(os.listdir()[x],text)
