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

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        print("�����Ŀ�ζ�У�")
        for flavor in self.flavors:
            print(flavor)
            

ice_cream = IceCreamStand("����˹�","���")
ice_cream.flavors = ["�㽶","ƻ��","����","����"]
ice_cream.show_flavors()
