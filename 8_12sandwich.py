# -*- coding: GBK -*-
def add_to_sandwich(*adds):
    print("顾客要在三明治中添加的实物有：")
    for add in adds:
        print(add)

add_to_sandwich("beef")
add_to_sandwich("chicken","vegetables")
add_to_sandwich("salt","tomato","orange")
    
