# -*- coding: GBK -*-

def make_car(a_brand,a_model,**cars_info):
    car = {}
    car["brand"] = a_brand
    car["model"] = a_model
    for key,value in cars_info.items():
        car[key] = value
    return car
car = make_car("����","X5",color = "��ɫ",price = "23��")
print(car)
        
