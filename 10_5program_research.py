# -*- coding: GBK -*
import readline
while True:
    reply = input("���������Ȱ���̵����ɣ���q�˳���\n")
    if reply == 'q':
        break
    else:
        reason = reply
        filename = "reasons.txt"
        with open(filename,'a') as file_object:
            file_object.write(reason + "\n")
            
print("�ټ���")
