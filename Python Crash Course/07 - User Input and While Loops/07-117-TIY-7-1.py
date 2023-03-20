# rental car
carchoice =  input("Please enter the make of the vehicle you'd like to rent\nMAKE:")

subaru_inventory = 13

toyota_inventory = 4

ford_inventory = 0

if carchoice.lower() == "subaru":
    if subaru_inventory > 0:
        print(f"\nLooks like we have {subaru_inventory} available!")
    else: 
        print(f"Unfortunately we are out of {carchoice.title()}s")
elif carchoice.lower() == "toyota":
    if toyota_inventory > 0:
        print(f"\nLooks like we have {toyota_inventory} available!")
    else: 
        print(f"Unfortunately we are out of {carchoice.title()}s")
elif carchoice.lower() == "ford":
    if ford_inventory > 0:
        print(f"\nLooks like we have {ford_inventory} available!")
    else: 
        print(f"Unfortunately we are out of {carchoice.title()}s")
else:
    print(f"\nUnfortunately we don't have that make available for rental")