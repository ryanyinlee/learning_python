# 6-9 Favorite Places

favorite_places = {
    "ryan": ["pakistan", "iraq", "syria"],
    "mish": ["ireland", "south korea", "california"],
    "me-me": ["the floor"],
}

for key, list in favorite_places.items():
    print(f"\n{key.title()}'s Favorite Places Are: ")
    for place in list:
        print(f"\t{place.title()}")