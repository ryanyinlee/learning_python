#8-14 cars

def car_info(manufacturer, model, **kwargs):
    """Takes vehicle information in and stores it in a dictionary and displays it"""
    kwargs['Make'] = manufacturer
    kwargs['Model'] = model
    return kwargs

newcar = car_info('subaru', 'crosstrek', color='white', tow_package=False)

print(newcar)