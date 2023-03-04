aliens = []

for alien_no in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'purple'
        alien['speed'] = 'medium'
        alien['points'] = 12

for alien in aliens[:10]:
    print(alien)