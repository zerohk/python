# -*- coding: GBK -*
def read_file(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.readlines()
            for content in contents:
                print(content)
    except FileNotFoundError:
        #print("�ļ�" + filename + "�����ڣ�")
        pass

read_file("cats.txt")
