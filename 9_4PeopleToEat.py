# -*- coding: GBK -*-
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("�͹ݵ������ǣ�" + self.name)
        print("�͹ݵ�ʳ�������ǣ�" + self.type)
        
    def open_restaurant(self):
        print("\n�͹�����Ӫҵ")
        
    def increment_number_served(self,incre):
        self.number_served += incre 
        
restaurant = Restaurant("����˹�","���")
print("��" + str(restaurant.number_served) + "������")


restaurant.number_served = 300
print("������" + str(restaurant.number_served) + "������")

restaurant.increment_number_served(200)
print("�������ÿ���ܽӴ�" + str(restaurant.number_served) + "��")

