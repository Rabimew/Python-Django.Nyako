import os
import time
a='现在可以使用telegram的机器人添加日志辣|让机器人在指定目录下塞进去了指定格式的文件XD！！'
fengefu = (a).index('|')
biaoti = (a)[0:fengefu - 1]
neirong = (a)[fengefu + 1:]
filePath = "../Nyako/rizhis/" + biaoti + "/"
state = os.path.exists(filePath)  # 判断路径是否存在
if state:
    print("File Exist!")
else:
    os.makedirs(filePath)  # 创建目录
    fileName = biaoti + '.txt'
    f = open(filePath + fileName, 'w', encoding='utf-8')
    pinglun = open(filePath + 'pinglun.txt', 'w', encoding='utf-8')
    note = neirong
    f.write(note)
    pinglun.write("")
