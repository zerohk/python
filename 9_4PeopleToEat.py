# -*- coding: GBK -*-
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("餐馆的名字是：" + self.name)
        print("餐馆的食物类型是：" + self.type)
        
    def open_restaurant(self):
        print("\n餐馆正在营业")
        
    def increment_number_served(self,incre):
        self.number_served += incre 
        
restaurant = Restaurant("家乡菜馆","湘菜")
print("有" + str(restaurant.number_served) + "人来过")


restaurant.number_served = 300
print("现在有" + str(restaurant.number_served) + "人来过")

restaurant.increment_number_served(200)
print("这个饭馆每天能接待" + str(restaurant.number_served) + "人")

