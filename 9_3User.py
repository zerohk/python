# -*- coding: GBK -*

class User():
    def __init__(self,first_name,last_name,sex,age,location):
        self.f_name = first_name
        self.l_name = last_name
        self.sex = sex
        self.age = age
        self.location = location
    
    
    def describe_user(self):
        print("������" + self.l_name + self.f_name)
        print("�Ա�" + self.sex)
        print("���䣺" + str(self.age))
        print("������" + self.location)
        
        
    def greet_user(self):
        print("���," + self.l_name + self.f_name)
        


user_1 = User("�Ƴ�","��","��",22,"����")
user_2 = User("��","��","Ů",23,"����")

user_1.describe_user()
user_2.describe_user()
