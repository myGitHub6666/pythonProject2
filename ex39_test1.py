# createc a mapping of state to abbreviation
states = {
    'orange': 'or',
    'florida': 'fl',
    'california': 'ca',
    'new york': 'ny',
    'michigan': 'mi'
}

# create a basic set of states and some cities in them
cities = {'ca': 'san francisco', 'mi': 'detroit', 'fl': 'jacksonville', 'ny': 'new york', 'or': 'portland'}

# add some more cities

# print out some cities
print('-' * 10)
print('ny state has:', cities['ny'])
print('or state has:', cities['or'])

# print some states
print('-' * 10)
print("michigan's abbreviation is :", states['michigan'])
print("florida's abbreviation is :", states['florida'])

# do it by using the state then cities dice
print('-' * 10)
print("michigan has:", cities[states['michigan']])
print("florida has:", cities[states['florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(cities.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every citiy in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {city[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('texas')

if not state:
    print("sorry,no texas")

# get a city with a default value
city = cities.get('tx', 'does not exist')
print(f"the city for state 'tx' is :{city}")
