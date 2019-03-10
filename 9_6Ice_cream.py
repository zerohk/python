# -*- coding: GBK -*-
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe_restaurant(self):
        print("餐馆的名字是：" + self.name)
        print("餐馆的食物类型是：" + self.type)
        
    def open_restaurant(self):
        print("\n餐馆正在营业")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        print("包含的口味有：")
        for flavor in self.flavors:
            print(flavor)
            

ice_cream = IceCreamStand("家乡菜馆","湘菜")
ice_cream.flavors = ["香蕉","苹果","菠萝","西瓜"]
ice_cream.show_flavors()
