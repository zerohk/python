# -*- coding: GBK -*-
class Dog():
    """ģ��С����һ��ʵ��"""
    def __init__(self,name,age):
        """��ʼ������name��age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """ģ��С������"""
        print(self.name + "��������")
        
    def roll(self):
        """ģ��С�����"""
        print(self.name + "���ڴ��")


my_dog = Dog('С��',3)
ur_dog = Dog('С��',5)

print("�ҵĹ����ֽ���" + my_dog.name + ",������" + str(my_dog.age) + "����")
my_dog.sit()
my_dog.roll()


print("��Ĺ����ֽ���" + ur_dog.name + ",������" + str(ur_dog.age) + "����")
ur_dog.sit()
ur_dog.roll()
