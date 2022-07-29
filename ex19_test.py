def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party")
    print("get a blanket.\n")


print("we can just give the function numbers directly:")
# 直接将数据进行传参
cheese_count_1 = int(input("请输入："))
boxes_of_crackers_1 = int(input("请输入："))
cheese_and_crackers(cheese_count_1, boxes_of_crackers_1)


print("or, we can use variables from our script:")
# 用变量进行传参,改为自动输入获取数据
amount_of_cheese = int(input(f"请输入{cheese_count_1}："))
amount_of_crackers = int(input("请输入："))
print(f"{input()}")
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too:")
# 用数学表达式进行传参
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two,variable and math:")
# 用变量和数学表达式组合进行传参，这里的amount_of_cheese和amount_of_crackers的值是14，15行赋值的
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# cheese_and_crackers(cheese_count + 100, boxes_of_crackers + 1000) 这里为什么不能替代原来的参数名称。、

