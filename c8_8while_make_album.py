# -*- coding: GBK -*-
def make_album(name,singer):
    album = {"a_name":name,"a_singer":singer}
    return album
    
while True:
    print("\nPlease input the album name,enter q to quit:")
    name = input("Album name:")
    if name == "q":
        break
    
    print("\nPlease input the singer name,enter q to quit:")
    singer = input("Singer name:")
    if singer == "q":
        break
    album = make_album(name,singer)
    print(album)
    
