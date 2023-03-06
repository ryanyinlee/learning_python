#movie tickets
from datetime import datetime

current_dateTime = datetime.now()

# under 3 = free
pricesub3 = 'free'
# 3-12 $10
price3thru12 = "$10"
# over 12 $15
priceover12 = "$15"

prompt = "Hello movie patron. What is your age?"

prompt += "\nAGE: "

active = True
#ask age

while active:
    age = input(prompt)
   
    if age == 'quit':
        active = False
    
    elif int(age) <= 3:
        print(f"Good news! Your ticket is {pricesub3}")
        
    elif int(age) > 3 and int(age) <= 12:
        print(f"Your ticket will be {price3thru12}")
        
    elif int(age) > 12:
        print(f"Your ticket will be {priceover12}")
        
    else:
        print(f"Sorry, I don't understand that input.")


#tell them cost of ticket

