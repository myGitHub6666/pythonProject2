# enumerate的用法
tuple1 = ('a','s','d')
dic1 = {'name':'lucy','age':'66'}
for tup in enumerate(tuple1):
    print(tup)

for index,value1 in enumerate(dic1):
    print(index,value1)

# set 用法
set1 = {1,2,3,4,5,3,2,4,"a","s"}
list1 = [1,2,4,1,3,4,6,74,3,2,1,2]
set2 = set(list1)
list1 = list(set2)
print(list1)
print(set2)

set1.pop()
print(set1)
set1.pop()
print(set1)


