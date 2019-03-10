# -*- coding: GBK -*-
"""一个用于描述饭店的类"""
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe_restaurant(self):
        print("餐馆的名字是：" + self.name)
        print("餐馆的食物类型是：" + self.type)
        
    def open_restaurant(self):
        print("\n餐馆正在营业")
