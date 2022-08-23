# 多态
class Animal:
    def say_hello(self):
        print("hello")


class Duck(Animal):
    def say_hello(self):
        print('hello 我是一只鸭子')


class Monkey(Animal):
    def say_hello(self):
        print("hello 我是一只猴子")


class Sheep(Animal):
    def say_hello(self):
        print("hello 我是一只羊")


# 通过此函数可以进行批量调用鸭子类型，不管对象是谁,只要拥有say_hello方法就可以被调用
def comm(obj):
    obj.say_hello()


obj1 = [Duck(), Monkey(), Sheep()]
for iterm in obj1:
    comm(iterm)
