# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print('i got nothing')


print_two("11","22")
print_two_again("33", "44")
print_one("55")
print_none()
