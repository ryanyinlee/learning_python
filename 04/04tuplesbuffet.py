#4-13

basic_foods = ("potatoes", "\"meat\"", "vegetables", "water", "bread")

print("This restaurant offers the following: ")

for food in basic_foods:
    print(f"You can get {food}")

"""basic_foods[1] = "real meat""" 

#can't do

#replace menu item by rewriting touble

basic_foods = ("potatoes", "\"real meat\"", "pie", "water", "bread")

print("\nThis restaurant offers the following: ")

for food in basic_foods:
    print(f"You can get {food}")
