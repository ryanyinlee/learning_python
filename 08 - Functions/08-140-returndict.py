def build_person(first_name, last_name, age=None):
    """Return a dictionary of info about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('james', 'hendrickson', 43)

print(musician)