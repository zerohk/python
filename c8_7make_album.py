# -*- coding: GBK -*-
def make_album(name,singer):
    album = {"a_name":name,"a_singer":singer}
    return album

album_1 = make_album("��ǧ����","����")
album_2 = make_album("��Ȼ����","������")
album_3 = make_album("����ת��","����Ѹ")

print(album_1)
print(album_2)
print(album_3)


def make_album_1(name,singer,songs=""):
    album = {"a_name":name,"a_singer":singer}
    if songs:
        album["a_songs"] = songs
    return album

album_4 = make_album_1("��ǧ����","����","7")
album_5 = make_album_1("��Ȼ����","������")
album_6 = make_album_1("����ת��","����Ѹ")

print(album_4)
print(album_5)
print(album_6)
        


