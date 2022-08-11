class Car:
    wheels = 3

    def __init__(self, name):
        self.name = name
        print(f"这个车的颜色是{self.name}")


car1 = Car('xiaoxin')
car2 = Car('xiaohong')
print(car2.wheels)
print(car1.wheels)
Car.wheels = 2
print(car1.wheels)
print(car1.name)
car1.name = " 8888 "
print(car1.name)

