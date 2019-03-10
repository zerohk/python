# -*- coding: GBK -*

class User():
    """一个用户类"""
    def __init__(self,first_name,last_name,sex,age,location):
        """初始化用户的各个属性"""
        self.f_name = first_name
        self.l_name = last_name
        self.sex = sex
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    
    def describe_user(self):
        """打印用户的基本信息"""
        print("姓名：" + self.l_name + self.f_name)
        print("性别：" + self.sex)
        print("年龄：" + str(self.age))
        print("地区：" + self.location)
        
        
    def greet_user(self):
        """向用户打招呼"""
        print("你好," + self.l_name + self.f_name)
        
    
    def increment_login_attempts(self):
        """增加用户尝试登录次数"""
        self.login_attempts += 1
        
        
    def reset_login_attempts(self):
        """重置尝试登录次数"""
        self.login_attempts = 0

user_1 = User("制成","沈","男",22,"湖南")
print("尝试登录次数为：" + str(user_1.login_attempts))
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("尝试登录次数为：" + str(user_1.login_attempts))
user_1.reset_login_attempts()
print("尝试登录次数为：" + str(user_1.login_attempts))

