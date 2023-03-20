#6-11 Cities

cities = {
    'seattle': {
        'country': 'usa',
        'population': 'lorj',
        'fact': 'stinky',
    },
    'bothell': {
        'country': 'usa',
        'population': 'smol',
        'fact': 'spendy',
    },
    'lynnwood': {
        'country': 'estados unidos',
        'population': 'mid',
        'fact': 'gross',
    },
}

for city, info in cities.items():
    print(f"{city.title()}")
    country = f"{info['country']}"
    population = f"{info['population']}"
    fact = f"{info['fact']}"

    if country == "usa":
        print(f"\t Located in: {country.upper()}")
    else:
        print(f"\t Located in: {country.title()}")
        
    print(f"\t Population: {population.title()}")
    print(f"\t Fact About It: {fact.title()}")