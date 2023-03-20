def city_country(city, country):
    """Returns a string in the form of City, Country"""
    cityname = city
    countryname = country
    fullname = f"{cityname}, {countryname}"
    return fullname.title()

print(city_country("santiago", "chile"))