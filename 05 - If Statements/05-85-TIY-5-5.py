#5-5 Alien Colors if-elif-else

alien_color = 'red'

if alien_color == 'green':
    points = 5
    print("Green hit!")
elif alien_color == 'yellow':
    print("Yellow hit!")
    points = 10
elif alien_color == "red":
    print("Red hit!")
    points = 15

print(f"You have earned {points} points!")