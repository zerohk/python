# -*- coding: GBK -*
def count_words(filename):
    """"����ͳ���ı�������"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "�Բ����ļ�" + filename + "�����ڣ�"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("�ļ�" + filename + "�������" + str(num_words) + "����")

filenames = ["Alice in Wonderland.txt","Siddhartha.txt","Moby Dick.txt","Little Women.txt"]
for filename in filenames:
    count_words(filename)
