alien_0 = {'color': 'green', 'speed': 5}

"""print(alien_0['points'])
"""

points = alien_0.get('points', 'Nothing exists. Do we even exist?')

print(points)

points2 = alien_0.get('points')

print(points2)