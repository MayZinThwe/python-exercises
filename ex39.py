#create a mapping of state toabbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }
#create a basic set of states and some cities in them
cities ={
        'CA':'SanFrancisco',
        'MI':'Detroit',
        'FL':'Jacksnoville'
        }

#add some more cities
cities['NY'] = 'New Yourk'
cities['OR'] = 'Portland'

#print out some cities
print("NY state has: ",cities['NY'])
print("OR state has: ",cities['OR'])

#print some states
print('_' * 10)
print("Michigan's abbreviation is: ",states['Michigan'])
print("Florida's abbreviation is: ",states['Florida'])

#do it by using the state then cities dict
print('_'*10)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ",cities[states['Florida']])

#print every state abbreviation
print('_'*10)
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state  
print('_'*10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has th city {city}")

#now do both at the same time
print('_'*10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('_'*10)
#safely get a abbreviation by state that might not be there 
state = states.get('Texas')
if not state:
    print("Sorry , no Texas.")

#get a city with a default value
city = cities.get('TX', 'Does not Exit')
print(f"The city for the state 'TX' is:{city}")

