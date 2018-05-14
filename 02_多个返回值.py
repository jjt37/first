def measure():
    '''测试温度和湿度'''

    print("测试开始。。。")
    temp=39
    wetness=50
    print("测量结束。。。")

    #可以用元组让函数一次返回多个参数
    #如果函数返回的是元祖，小括号可以省略
    return temp,wetness

result=measure()
print(result[0])
print(result[1])

#使用多个变量接受元组
gl_temp,gl_wetness=measure()

print(gl_temp)
print(gl_wetness)