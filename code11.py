# 创建一个Animal类，实例化一个cat对象，请给cat对象动态绑定一个run方法，给类绑定一个类属性colour，给类绑定一个类方法并打印ok
import types


def run(self):
    print("小猫快跑")


@classmethod
def info(cls):
    print("ok")


class Animal:
    pass


# 直接把方法info绑定到类方法inf
Animal.inf = info
# 直接把red绑定到colour属性上
Animal.colour = "red"
cat = Animal()
cat.run = types.MethodType(run, cat)
cat.run()
print(cat.colour)
# 实例对象调用类方法inf
cat.inf()

