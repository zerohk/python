# -*- coding: GBK -*
"""描述管理员及其权限的类"""
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
        self.privileges = ["添加评论","删除评论","删除用户"]
    
    
    def show_privileges(self):
        print("管理员的权限有：")
        for privilege in self.privileges:
            print(privilege)
