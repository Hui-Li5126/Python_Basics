#dictionaries
#you can only use numbers to get items out of a Lists
#A dict lets you use anything, not just numbers.
#list vs dictionaries
  #A list is for an ordered list of items, dict is for matching some items (called keys)
     #to other items (called "values")
  #collections.OrderedDict data structure
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
  }

cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
  }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has ", cities[states['Florida']])

print('-'*10)

#dict.items() displays a list of a given dictionary's (key, value) tuple pair.
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
