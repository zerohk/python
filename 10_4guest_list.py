# -*- coding: GBK -*
import readline
while True:
    name = input("请输入你的名字，按q退出：\n")
    if name == 'q':
        break
    else:
        guest_name = name
        print("你好，" + guest_name + "!\n")
        filename = "guestlist.txt"
        with open(filename,'a') as file_object:
            file_object.write(guest_name + "\n")
            
print("再见！")
    
