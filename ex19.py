def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party")
    print("get a blanket.\n")


print("we can just give the function numbers directly:")
# 直接将数据进行传参
cheese_and_crackers(20, 30)

print("or, we can use variables from our script:")
# 用变量进行传参
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too:")
# 用数学表达式进行传参
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two,variable and math:")
# 用变量和数学表达式组合进行传参，这里的amount_of_cheese和amount_of_crackers的值是14，15行赋值的
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# we can just give the function numbers directly:
# you have 20 cheeses!
# you have 30 boxes of crackers!
# man that's enough for a party
# get a blanket.
#
# or, we can use variables from our script:
# you have 10 cheeses!
# you have 50 boxes of crackers!
# man that's enough for a party
# get a blanket.
#
# we can even do math inside too:
# you have 30 cheeses!
# you have 11 boxes of crackers!
# man that's enough for a party
# get a blanket.
#
# and we can combine the two,variable and math:
# you have 110 cheeses!
# you have 1050 boxes of crackers!
# man that's enough for a party
# get a blanket.
