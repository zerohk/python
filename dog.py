# -*- coding: GBK -*-
class Dog():
    """模仿小狗的一次实践"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗坐下"""
        print(self.name + "正在坐着")
        
    def roll(self):
        """模拟小狗打滚"""
        print(self.name + "正在打滚")


my_dog = Dog('小白',3)
ur_dog = Dog('小黑',5)

print("我的狗名字叫做" + my_dog.name + ",他今年" + str(my_dog.age) + "岁了")
my_dog.sit()
my_dog.roll()


print("你的狗名字叫做" + ur_dog.name + ",他今年" + str(ur_dog.age) + "岁了")
ur_dog.sit()
ur_dog.roll()
