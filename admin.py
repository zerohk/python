# -*- coding: GBK -*
"""��������Ա����Ȩ�޵���"""
from user import User

class Admin(User):
    def __init__(self,first_name,last_name,sex,age,location):
        super().__init__(first_name,last_name,sex,age,location)
        self.f_name = first_name
        self.l_name = last_name
        self.sex = sex
        self.age = age
        self.location = location
        self.privileges = Privileges()
        

class Privileges():
    def __init__(self):
        self.privileges = ["�������","ɾ������","ɾ���û�"]
    
    
    def show_privileges(self):
        print("����Ա��Ȩ���У�")
        for privilege in self.privileges:
            print(privilege)
