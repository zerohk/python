# -*- coding: GBK -*-
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe_restaurant(self):
        print("�͹ݵ������ǣ�" + self.name)
        print("�͹ݵ�ʳ�������ǣ�" + self.type)
        
    def open_restaurant(self):
        print("\n�͹�����Ӫҵ")


restaurant = Restaurant("����˹�","���")
print("���֣�" + restaurant.name)
print("���ͣ�" + restaurant.type)
print("\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
