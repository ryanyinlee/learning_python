from random import choice

lottery = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')

my_ticket = []

winning_ticket = []

tries = 0

for i in range(4):
    my_ticket.append(choice(lottery))
 
print(f"Your ticket is {my_ticket}")

traverse = True

while traverse:
    if winning_ticket != my_ticket:
        print(f"The winning ticket was {winning_ticket}, but no match!")
        winning_ticket.clear()
        tries += 1
        for i in range(4):
            winning_ticket.append(choice(lottery))
    else:
        print(f"The winning ticket was {winning_ticket}, matching your ticket of {my_ticket}")
        print(f"It took {tries} tries to get a match.")
        break
            
 
print(my_ticket)