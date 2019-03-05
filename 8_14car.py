# -*- coding: GBK -*-

def make_car(a_brand,a_model,**cars_info):
    car = {}
    car["brand"] = a_brand
    car["model"] = a_model
    for key,value in cars_info.items():
        car[key] = value
    return car
car = make_car("宝马","X5",color = "银色",price = "23万")
print(car)
        
