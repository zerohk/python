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


restaurant_1 = Restaurant("����˹�","���")
restaurant_2 = Restaurant("���Ϸ�","���")
restaurant_3 = Restaurant("����","����")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
