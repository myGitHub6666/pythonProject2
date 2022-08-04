print("""you enter a dark room with two doors.
do you go through door #1 or door #2?""")

door = int(input("请输入> "))  # input获取的数值直接赋值给door
print(f"door的数值是：{door}")
if door == 1 :
    print("there's a giant bear there eating a cheese cake")
    print("what do you do?")
    print("1. take the cake")
    print("2. scream at the bear.")

    bear = int(input("> "))

    if bear == 1 :
        print("the bear eats your face off. goof job")
    elif bear == 2 :
        print("the bear eats your legs off. good job")
    else:
        print(f"well, doing {bear} is probably better")
        print("bear runs away.")

elif door == "2":
    print("you stare into the endless abyss at cthulhu's retina.")
    print("1. Blueberries.")
    print("2. yellow jacket clothespins")
    print("3. understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello")
        print ("good job")
    else:
        print("the insanity rots your eyes into a pool of muck ")
        print("good job")

else:
    print("you stumble around and fall on a knife and die. good job")


