#8-12 user profile

def build_profile(first, last, **user_info):
    """Build a dictionary with everything input about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('ryan', 'lee', location='lynnwood', field = 'programmer', birds=4)

print(user_profile)