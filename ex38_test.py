stuff = '1 2 3 4 5'
other_stuff = '7,6,8,9'
one_stuff = stuff.split(' ')
print(one_stuff)
new_other_stuff = other_stuff.split(',')
print(new_other_stuff)
for i in new_other_stuff:
    print(i)
    one_stuff.append(i)
    print(one_stuff)

print(new_other_stuff)
print(one_stuff)
one_stuff.sort()
one_stuff.reverse()
print(one_stuff)

print(" ".join(one_stuff))






