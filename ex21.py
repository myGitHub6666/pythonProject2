def add(a, b):
    print(f"ADDING{a} +{b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING{a} - {b}")
    return a - b


# return  当函数结束的时候，他就可以将a  + b 的结果返回并可以赋值给一个变量。

def multiply(a, b):
    print(f"MULTIPLYING{a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVING{a} / {b}")
    return a / b


print("'let's do some math with just functions! ")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age:{age},height : {height},weight : {weight},iq :{iq}")

print("here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("that becomes:", what, "can you do it by hand?")
