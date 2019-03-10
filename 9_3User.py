# -*- coding: GBK -*

class User():
    def __init__(self,first_name,last_name,sex,age,location):
        self.f_name = first_name
        self.l_name = last_name
        self.sex = sex
        self.age = age
        self.location = location
    
    
    def describe_user(self):
        print("姓名：" + self.l_name + self.f_name)
        print("性别：" + self.sex)
        print("年龄：" + str(self.age))
        print("地区：" + self.location)
        
        
    def greet_user(self):
        print("你好," + self.l_name + self.f_name)
        


user_1 = User("制成","沈","男",22,"湖南")
user_2 = User("婷","冯","女",23,"海南")

user_1.describe_user()
user_2.describe_user()
