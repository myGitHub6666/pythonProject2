# createc a mapping of state to abbreviation
# 定义一个states字典。
states = {
    'orange': 'or',
    'florida': 'fl',
    'california': 'ca',
    'new york': 'ny',
    'michigan': 'mi'
}

# create a basic set of states and some cities in them
# 定义一个城市字典。
cities = {'ca': 'san francisco', 'mi': 'detroit', 'fl': 'jacksonville', 'ny': 'new york', 'or': 'portland'}

# add some more cities

# print out some cities
print('-' * 10)
# 打印城市名称
print('ny state has:', cities['ny'])
print('or state has:', cities['or'])

# print some states
print('-' * 10)
# 打印州的名称
print("michigan's abbreviation is :", states['michigan'])
print("florida's abbreviation is :", states['florida'])

# do it by using the state then cities dice
print('-' * 10)
#  打印cities
print("michigan has:", cities[states['michigan']])
print("florida has:", cities[states['florida']])
print(cities)

# print every state abbreviation
print('-' * 10)
#  将字典转换为元租形式的一个列表
print(cities.items())
for state in list(cities.items()):
    # 这样取出来的值，是元祖形式。
    print(state)
    for a in state:
        print(a)

    # print(f"{state} is abbreviated {abbrev}")

# print every citiy in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('texas')
print(states.keys())
print(states.values())
if not state:
    print("sorry,no texas")


# get a city with a default value
# 获取tx对应的值，如果不存在，则返回don’t exist）
city = cities.get('tx', 'does not exist')
print(f"the city for state 'tx' is :{city}")

tuple1 = (1,2,3,4)
for s in tuple1:
    print(s)
list1 = [('name','xiaoming','a'),('age',4,3),('city','xian',4)]
for x in list1:
    print(x)
for a,b, c in list1:
    print(a,b,c)



