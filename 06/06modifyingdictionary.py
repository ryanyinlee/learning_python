alien_0 = {'x': 0, 'y': 25, 'speed': 'medium'}

print(f"Old pos: {alien_0['x']}")

#move alien right based on speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

# old pos plus increment = new pos

alien_0['x'] = alien_0['x'] + x_increment

print(f"New pos: {alien_0['x']}")

alien_0['speed'] = 'fast'

#move alien right based on speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x'] = alien_0['x'] + x_increment

print(f"New pos: {alien_0['x']}")
