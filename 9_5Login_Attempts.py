# -*- coding: GBK -*

class User():
    """һ���û���"""
    def __init__(self,first_name,last_name,sex,age,location):
        """��ʼ���û��ĸ�������"""
        self.f_name = first_name
        self.l_name = last_name
        self.sex = sex
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    
    def describe_user(self):
        """��ӡ�û��Ļ�����Ϣ"""
        print("������" + self.l_name + self.f_name)
        print("�Ա�" + self.sex)
        print("���䣺" + str(self.age))
        print("������" + self.location)
        
        
    def greet_user(self):
        """���û����к�"""
        print("���," + self.l_name + self.f_name)
        
    
    def increment_login_attempts(self):
        """�����û����Ե�¼����"""
        self.login_attempts += 1
        
        
    def reset_login_attempts(self):
        """���ó��Ե�¼����"""
        self.login_attempts = 0

user_1 = User("�Ƴ�","��","��",22,"����")
print("���Ե�¼����Ϊ��" + str(user_1.login_attempts))
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("���Ե�¼����Ϊ��" + str(user_1.login_attempts))
user_1.reset_login_attempts()
print("���Ե�¼����Ϊ��" + str(user_1.login_attempts))

