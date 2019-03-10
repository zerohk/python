# -*- coding: GBK -*
def count_words(filename):
    """"用来统计文本单词数"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "对不起，文件" + filename + "不存在！"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("文件" + filename + "包含大概" + str(num_words) + "个字")

filenames = ["Alice in Wonderland.txt","Siddhartha.txt","Moby Dick.txt","Little Women.txt"]
for filename in filenames:
    count_words(filename)
