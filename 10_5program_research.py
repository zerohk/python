# -*- coding: GBK -*
import readline
while True:
    reply = input("请输入你热爱编程的理由，按q退出：\n")
    if reply == 'q':
        break
    else:
        reason = reply
        filename = "reasons.txt"
        with open(filename,'a') as file_object:
            file_object.write(reason + "\n")
            
print("再见！")
