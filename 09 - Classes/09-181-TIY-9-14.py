from random import choice

lottery = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')

lottery_result = []

x = 4

while x > 0:
    result = choice(lottery)
    lottery_result.append(result)
    x = x - 1

print(f"If your ticket matches {lottery_result}, you win a prize!")