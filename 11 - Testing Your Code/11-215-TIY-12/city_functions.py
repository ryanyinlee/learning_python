def city_country(city, country, population=""):
    """Returns a string in the form of City, Country"""
    cityname = city
    countryname = country
    if population:
        populationcount = population
        fullname = f"{cityname}, {countryname} Population: {populationcount}"
    else:
        fullname = f"{cityname}, {countryname}"
    return fullname.title()

