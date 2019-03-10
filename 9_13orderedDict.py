from collections import OrderedDict

prog_dic = OrderedDict()
prog_dic["c"] = "a basic language"
prog_dic["java"] = "an oop language"
prog_dic["python"] = "a very useful language"
prog_dic["android"] = "a famous language"

for language,define in prog_dic.items():
    print(language + " is " + define)
