# -*- coding: GBK -*
filename = "Alice in Wonderland.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "�Բ����ļ�" + filename + "�����ڣ�"
    print(msg)
else:
    words = contents.split()
    #���÷���split()��������һ���б����а����ⲿͯ���е����е��ʡ�
    num_words = len(words)
    print("�ļ�" + filename + "�������" + str(num_words) + "����")
