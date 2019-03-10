# -*- coding: GBK -*
def read_file(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "对不起，文件" + filename + "不存在！"
        print(msg)
    else:
        num = contents.lower().count("the")
        print("在文件" + filename + "中，‘the’ 出现了" + str(num) + "次")
        
read_file("Alice in Wonderland.txt")
        
