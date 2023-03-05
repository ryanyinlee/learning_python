# 6-10 Favorite Numbers

fave_nums = {
    'steven': [69, 100, 1000],
    'ptheven': [420, 69, 77, 44],
    'pthaulisyius': [1000, 10, 0.001],
    'samsonite': [4,3, 2, 1],
    'bill': [13, 777, 1800, 80085],
}

for person, nums in fave_nums.items():
    print(f"\n{person.title()}'s Favorite Numbers are:")
    for num in nums:
        print(f"\t{num}")