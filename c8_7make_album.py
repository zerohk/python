# -*- coding: GBK -*-
def make_album(name,singer):
    album = {"a_name":name,"a_singer":singer}
    return album

album_1 = make_album("大千世界","许嵩")
album_2 = make_album("依然爱你","王力宏")
album_3 = make_album("爱情转移","陈奕迅")

print(album_1)
print(album_2)
print(album_3)


def make_album_1(name,singer,songs=""):
    album = {"a_name":name,"a_singer":singer}
    if songs:
        album["a_songs"] = songs
    return album

album_4 = make_album_1("大千世界","许嵩","7")
album_5 = make_album_1("依然爱你","王力宏")
album_6 = make_album_1("爱情转移","陈奕迅")

print(album_4)
print(album_5)
print(album_6)
        


