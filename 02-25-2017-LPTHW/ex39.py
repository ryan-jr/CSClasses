# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:04:15 2017

@author: rjr

Covering dicts
"""



# Mapping states to abbreviations
states = {
        "Oregon": "OR",
        "Florida": "FL",
        "Arizona": "AZ",
        "Iowa": "IA",
        "Kansas": "KS"
        }

# States and cities in them
cities = {
        "CA": "San Francisco",
        "OR": "Portland",
        "KS": "Topeka",
        "FL": "Miami"
        }

cities["NY"] = "New York"
cities["MT"] = "Billings"


print("-" * 10)
print("NY state has: ", cities["NY"])
print("OR state has: ", cities["OR"])

print("-" * 10)
print("Arizona's abbreviation is: ", states["Arizona"])
print("Florida's abbreviation is: ", states["Florida"])

print("-" * 10)
print("CA has: ", cities[states["Oregon"]])
print("FL has: ", cities[states["Florida"]])

print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print("-" * 10)
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")
    
city = cities.get("TX", "Does not Exist")
print(f"The city for the state 'TX' is {city}")

print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev} and has city {cities[abbrev]}")
    print("%%%")
    

    


        

