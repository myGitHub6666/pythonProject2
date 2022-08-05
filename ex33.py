numbers = []


def for_number(num, k):
    i = 0
    while i < num:
        numbers.append(i)
        i += k
        print("-----")
    return numbers


#
# while i in range(0, 7):
# while i < num:
#     print(f"at the top i is {i}")
#     numbers.append(i)
#
#     i += 1
#     print("numbers now:",numbers)
#     print(f"at the bottom i is {i}")
print("<<<<<<:", for_number(6, 2))
print("the numbers:")
for number in numbers:
    print(number)
