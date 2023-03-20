def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a neatly formatted full name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('real', 'live', 'musician')

print(musician)

musician = get_formatted_name('real', 'musician')

print(musician)