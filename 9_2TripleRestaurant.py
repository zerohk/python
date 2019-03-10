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


restaurant_1 = Restaurant("家乡菜馆","湘菜")
restaurant_2 = Restaurant("螺蛳粉","桂菜")
restaurant_3 = Restaurant("肠粉","粤菜")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
