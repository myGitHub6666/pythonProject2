# 决战紫禁之巅有两个人物，西门吹雪，叶孤城
# 属性：name 玩家的名字，blood玩家的血量
# 方法：tong()对方一刀，掉10滴血，kanren()砍对方一刀，掉15滴血，chiyao()吃一颗药，补10滴血。__str__()打印玩家状态

class Person:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood

    def tong(self, enemy):
        enemy.blood -= 10
        print(f"{self.name}捅了{enemy.name}一刀")

    def kanren(self, enemy):
        enemy.blood -= 15
        print(f"{self.name}砍了{enemy}一刀")

    def chiyao(self):
        self.blood += 10
        print(f"{self.name}吃了一颗药丸")

    def __str__(self):
        return f"{self.name}还有{self.blood}血"


p1 = Person("西门吹雪", 100)
p2 = Person("叶孤城", 100)
n = 0
while True:
    p1.tong(p2)
    print(p1)
    print(p2)
    p2.chiyao()
    print(p2)
    p2.tong(p1)
    print(p2)
    print(p1)
    n += 1
    print(f"**第一个{n}个回和结束**")
    if p1.blood <= 0 or p2.blood <= 0:
        print("游戏结束")
        break
print("退出游戏")
print(p1.blood)

# for p1.blood >= 0 and p2.blood >= 0 : 用for循环咋写？？？？？？
