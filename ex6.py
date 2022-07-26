# 定义一个变量10
types_of_people = 10
# 给x定义一个字符串，在python中字符串，以f开头，包含{}的表达式，
# 在程序运行的时候会被表达式的值替代。
x = f"there are {types_of_people} types of people."
# 定义一个字符串 dinary
binary = 'binary'
# 定义一个字符串do_not
do_not = "don't no"
# 定义一个字符串f
y =  f'those who know {binary} and those who {do_not}.'
# 打印x和打印y
print(x)
print(y)
# 打印 i said:x
print(f'I said:{x}')
print(f"I also said:'{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funnny? {}!"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
