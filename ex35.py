from sys import exit  # 引入sys部分模块exit


def gold_room():     # 定义一个函数。
    print("this room is full of gold. how much do you take?")  # 打印出一句提示信息

    choice = input("> ")  # 从input函数输入数据，并赋值给choice这个变量
    if "0" in choice or "1" in choice:  # 如果输入的是0 或者1
        how_much = int(choice)  # 就将chioce的值转换成整数型，并赋值给how_much这个变量
    else:  # 如果输入的是其他是数据
        dead("man, learn to type a number") # 调用dead函数，并退出游戏。

    if how_much < 50:   # 如果how_much的值小于50，则打印出如下信息。并退出
        print("nice, you're not greedy, you win!")
        exit(0)
    else:  # 如果how_much的值是其他的，就直接调用dead函数，并退出函数
        dead("you greedy bastard")


def bear_room():     # 定义bear_room,并直接打出如下数据
    print("there is a bear here")
    print("the bear has a bunch of honey")
    print("the fat bear is in front of another door")
    print("hoe are you going to move the bear?")
    bear_moved = False  # 并对bear_room赋值False

    while True:  # 判断布尔表达式的真假，如果为True,则要一直循环到False为止
        choice = input("> ")  # 从input输入数据并赋值给chioce

        if choice == "take honey":   # choice的值是take honey，则调用dead函数打印如下数据并退出程序。
            dead("the bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved: # 如果choice的值是taunt bear，并且bear_moved的值不是False
            print("the bear has moved from the door")  # 打印
            print("you can go through it now") # 打印
            bear_moved = True  # 并且把bear_moved 的值改为True
        elif choice == "taunt bear" and bear_moved: # 如果choice的值是taunt bear 并且 bear_moved的值是t rue，则调用dead函数打印，并退出游戏
            dead("the bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:  # 如果choice的值是open door 并且 bear_moved为True，则调用gold_room
            gold_room()
        else: # 如果输入的是其他的数据，则直接打印。
            print("I got no idea what that means")


def cthulhu_room():     # 定义函数，并打印数据
    print("here y ou see the great evil cthulhu.")
    print("he,it ,whatever stares at you and you go insane")
    print("do you flee for your life or eat your head?")

    choice = input("> ")  # 从input输入数据并赋值给choice

    if "flee" in choice:    # 如果flee在choice值中，则调用stat函数
        start()
    elif "head" in choice:   # 如果head在choice值中则调用dead函数，并结束游戏
        dead("well that was tasty")
    else: # 如果输入的是其他数据则调用cthulhu_room函数
        cthulhu_room()


def dead(why):   # 定义dead函数的功能，传入位置参数输出打印
    print(why, "good job")
    exit(0)


def start():     # 定义start函数
    print("you are in a dark room")  # 打印
    print("there is a door to your right and left") # 打印
    print("which one do you take") # 打印

    choice = input("<")     # input输入数据并赋值给choice

    if choice == "left":     # 如果choice的值是left，则调用bear_room函数
        bear_room()
    elif choice == "right":  # 如果choice的值是right，则调用cthulhu_room函数
        cthulhu_room()
    else:   # 如果两个都不是，则调用dead函数
        dead("you stumble a around the room until you starve")


start()     # 调用start函数，开始游戏。
