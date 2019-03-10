# -*- coding: GBK -*
def read_file(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.readlines()
            for content in contents:
                print(content)
    except FileNotFoundError:
        #print("文件" + filename + "不存在！")
        pass

read_file("cats.txt")
