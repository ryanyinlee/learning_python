aliens = []

for alien_no in range(5):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


for alien_no in range(5):
    new_alien = {'color': 'purple', 'points': 12, 'speed': 'medium'}
    aliens.append(new_alien)


for alien in aliens[:10]:
    if alien['color'] == 'green':
        alien['color'] = 'purple'
        alien['speed'] = 'medium'
        alien['points'] = 12
    elif alien['color'] == 'purple':
        alien['color'] = 'chartreuse'
        alien['speed'] = 'realfast'
        alien['points'] = 10000



for alien in aliens[:10]:
    print(alien)