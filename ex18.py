# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")
# 函数之间必须要空两行


def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")


def print_one(arg1):
    print(f"arg1:{arg1}")


def print_none():
    print('i got nothing')


print_two("11", "22")
print_two_again("33", "44")
print_one("55")
print_none()

# arg1:11, arg2:22
# arg1:33, arg2:44
# arg1:55
# i got nothing
