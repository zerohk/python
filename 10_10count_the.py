# -*- coding: GBK -*
def read_file(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "�Բ����ļ�" + filename + "�����ڣ�"
        print(msg)
    else:
        num = contents.lower().count("the")
        print("���ļ�" + filename + "�У���the�� ������" + str(num) + "��")
        
read_file("Alice in Wonderland.txt")
        
