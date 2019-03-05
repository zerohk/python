# -*- coding: GBK -*-

magicians = ["刘谦","大卫科波菲尔","沈智承"]
new_magicians = []

def make_great(magicians,new_magicians):
    while magicians:
        current_magician = "伟大的" + magicians.pop()
        new_magicians.append(current_magician)
        
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians)
make_great(magicians[:],new_magicians)
show_magicians(new_magicians)
show_magicians(magicians)
