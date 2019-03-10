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
        
class Admin(User):
    def __init__(self,first_name,last_name,sex,age,location):
        super().__init__(first_name,last_name,sex,age,location)
        self.f_name = first_name
        self.l_name = last_name
        self.sex = sex
        self.age = age
        self.location = location
        self.privileges = ["�������","ɾ������","ɾ���û�"]
    
    
    def show_privileges(self):
        print("����Ա��Ȩ���У�")
        for privilege in self.privileges:
            print(privilege)
            
admin = Admin("��","��","Ů",23,"����")
admin.show_privileges()
        
