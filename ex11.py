print('how old are you?', end="")
age = int(input())
print("how tall are you?", end="")
height = int(input())
print("how much do you weight?", end="")
# input输入的是字符串类型，将其转化成int
weight = int(input())

print(f"so,you're {age} old,{height} tall and {weight} heavy.")

# how old are you?30
# how tall are you?1.7
# how much do you weight?80
# so,you're 30 old,1.7 tall and 80 heavy.
