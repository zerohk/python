# -*- coding: GBK -*-

magicians = ["��ǫ","�����Ʋ��ƶ�","���ǳ�"]
new_magicians = []

def make_great(magicians,new_magicians):
    while magicians:
        current_magician = "ΰ���" + magicians.pop()
        new_magicians.append(current_magician)
        
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians)
make_great(magicians[:],new_magicians)
show_magicians(new_magicians)
show_magicians(magicians)
