i = 1
mylist = []
for i in range(1, 5):
    mylist.append(i)
    i += 1
    print(mylist)

print(f"<<<<", mylist)
#
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# <<<< [1, 2, 3, 4]
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# <<<< [1, 2, 3, 4]