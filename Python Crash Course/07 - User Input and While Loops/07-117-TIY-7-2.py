# restaurant seating
from datetime import datetime

current_dateTime = datetime.now()

print(f"Today is {current_dateTime.month}, {current_dateTime.day}, {current_dateTime.year}\n")
print(f"The time is: {current_dateTime.hour}:{current_dateTime.minute}")

restaurant_name = "Taco Tim's"

seatingnumber = input(f"How many people would you like to seat at {restaurant_name} today?\nNumber In Party:")

seatingnumber = int(seatingnumber)

time_delay = 30

if seatingnumber > 8:
    print(f"Due to your party size you may have to wait up to 30 minutes for a table, is that okay?")
    reply = input("Yes/No:")
    if reply == "yes" or reply == "y":
        print(f"Excellent! Your table should be ready at {current_dateTime.hour}:{current_dateTime.minute + time_delay}")
    elif reply == "no" or reply == "n":
        print(f"I'm so sorry we couldn't seat you today! Please come back soon.")
    else:
        print(f"I'm sorry, I couldn't understand your response.")
else:
    print(f"Excellent, you will be seated shortly.")

