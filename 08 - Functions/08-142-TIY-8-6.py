#8-6 city names

def city_country(city, country):
    """Takes in name of a city and country and formats it neatly"""
    formatted = f"{city}, {country}"
    return formatted.title()


city1 = city_country("Reykjavik", "Iceland")
print(city1)