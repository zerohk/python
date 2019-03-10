# -*- coding: GBK -*
filename = "Alice in Wonderland.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "对不起，文件" + filename + "不存在！"
    print(msg)
else:
    words = contents.split()
    #调用方法split()，以生成一个列表，其中包含这部童话中的所有单词。
    num_words = len(words)
    print("文件" + filename + "包含大概" + str(num_words) + "个字")
