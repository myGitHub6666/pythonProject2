class Person:
    # 类属性
    colour = "red"

    def __init__(self, name, age):
        # 实例化对象属性
        self.name = name
        self.age = age

    def __new__(cls,*args,**kwargs):
        # 创建对象的过程
        print("new已经执行")
        return object.__new__(cls)

    def __str__(self):
        # 字符串化对象
        return f"{self.name}, {self.colour}, {self.age}"

    def eat(self, food):
        # 实例化对象的方法
        print(f"{self.name}喜欢吃{food},喜欢的颜色{self.colour}")


p1 = Person("小明", 9)
print(p1)
p1.eat("红苹果")
print(p1)