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
        
class Admin(User):
    def __init__(self,first_name,last_name,sex,age,location):
        super().__init__(first_name,last_name,sex,age,location)
        self.f_name = first_name
        self.l_name = last_name
        self.sex = sex
        self.age = age
        self.location = location
        self.privileges = ["添加评论","删除评论","删除用户"]
    
    
    def show_privileges(self):
        print("管理员的权限有：")
        for privilege in self.privileges:
            print(privilege)
            
admin = Admin("婷","冯","女",23,"海南")
admin.show_privileges()
        
