# 定义一个person类。类中要有初始化的方法，方法中要有姓名，年龄两个私有属性，
# 提供获取用户信息的函数
# 提供获取私有属性的方法
# 提供可以设置私有属性的方法
# 设置年龄在0-120的方法，如果不在这个范围不能设置成功
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"{self.__name}的年龄是{self.__age}"

    def getPersonName(self):
        return self.__name

    def getPersonAge(self):
        return self.__age

    def setPersonName(self,name):
        self.__name = name
        return self.__name

    def setPersonAge(self,age):
        if 0 < age < 120:
            self.__age = age
            # 只是进行设置，并不需要返回数据
            # return self.__age
        else:
            print("请重新设置年龄")




