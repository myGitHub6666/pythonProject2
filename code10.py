# 创建一个类。并定义两个私有化属性，提供一个获取属性和设置属性的方法，利用property属性给调用者提供属性的调用

class Person:
    def __init__(self):
        self.__name = "lucy"
        self.__age = 9

    @property  # 装饰器直接把方法转化为属性。
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self,name):
        self.__name = name

    @age.setter
    def age(self,age):
        self.__age = age

    def __str__(self):
        return f"{self.__name}的年龄是{self.__age}"


p = Person()
p.name = "zhangsan"
p.age = "12"
print(p)
print(p.name)