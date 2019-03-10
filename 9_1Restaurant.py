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


restaurant = Restaurant("家乡菜馆","湘菜")
print("名字：" + restaurant.name)
print("菜型：" + restaurant.type)
print("\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
