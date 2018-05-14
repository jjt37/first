#创建一个文件
f_r=open("jjt.txt","r")
f_w=open("jjt[附件】.txt","w")

while True:
    text = f_r.readline()
    if not text:
        break
    f_w.write(text)



f_w.close()
f_r.close()