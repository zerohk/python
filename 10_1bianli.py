# -*- coding: GBK -*
filename = "learning_python.txt"
with open(filename) as file_objec:
    for file in file_objec:
        print(file.rstrip())
