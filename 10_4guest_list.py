# -*- coding: GBK -*
import readline
while True:
    name = input("������������֣���q�˳���\n")
    if name == 'q':
        break
    else:
        guest_name = name
        print("��ã�" + guest_name + "!\n")
        filename = "guestlist.txt"
        with open(filename,'a') as file_object:
            file_object.write(guest_name + "\n")
            
print("�ټ���")
    
