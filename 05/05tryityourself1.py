#5-3 Alien Colors

alien_color = 'green'

if alien_color == 'green':
    points = 5
    print("Green hit!")

if alien_color == 'red':
    points = 5
    print("Red hit!")



print(f"You have earned {points} points!")

#5-4 Alien Colors if else

alien_color = 'fuschia'

if alien_color == 'green':
    points = 5
    print("Green hit!")
else:
    print("Non-green hit!")
    points = 10

print(f"You have earned {points} points!")

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