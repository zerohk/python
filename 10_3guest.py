# -*- coding: GBK -*
import readline
guest_name = input("请输入你的名字：")
filename = "guest.txt"
with open(filename,'a') as file_object:
    file_object.write(guest_name)
