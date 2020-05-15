import os
import time



filePath = "../Nyako/rizhis/测试日志/"
state = os.path.exists(filePath)  # 判断路径是否存在
if state:
    print("File Exist!")
else:
    os.makedirs(filePath)  # 创建目录
    fileName = '测试日志.txt'
    f=open(filePath + fileName, 'w',encoding='utf-8')
    pinglun = open(filePath +'pinglun.txt','w',encoding='utf-8')
    testNote = '测试文件'
    f.write(testNote)
    pinglun.write("")

