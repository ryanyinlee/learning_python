rivers_and_country = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'usa',
    'thames': 'uk',

}

for river, country in rivers_and_country.items():
    if country == "uk":
        print(f"The river {river.title()} runs through the {country.upper()}")
    elif country == "usa":
        print(f"The river {river.title()} runs through the {country.upper()}")
    else:
        print(f"The river {river.title()} runs through {country.title()}")

print(f"\nThe rivers in rivers_and_country are:")
for river in rivers_and_country.keys():
    print(f"{river.title()}")
    
print(f"\nThe countries in rivers_and_country are:")
for country in rivers_and_country.values():
    if country == "usa":
        print(country.upper())
    elif country == "uk":
        print(country.upper())
    else:
        print(f"{country.title()}")
    