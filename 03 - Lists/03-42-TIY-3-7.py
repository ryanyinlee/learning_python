#3-7 shrinking guest list

guest_list = []

guest_list.append('Douglas Adams')
guest_list.append('George Washington')
guest_list.append('Jesus Christ')

x = 0

while x < len(guest_list):
    print(f"Hello {guest_list[x]}, you are invited to dinner")
    x=x+1

y = 2

print(f"It looks like {guest_list[y]} can't make it.")

guest_list.remove('Jesus Christ')
guest_list.append('Mahatma Ghandi')


print(f"We are replacing them with {guest_list[y]} ")

x = 0
while x < len(guest_list):
    print(f"Hello {guest_list[x]}, you are invited to dinner")
    x=x+1


guest_list.insert(0, 'Buddha')
guest_list.insert(1, 'Linus Torvalds')
guest_list.append('Teddy Roosevelt')

x = 0
while x < len(guest_list):
    print(f"Hello {guest_list[x]}, you are invited to dinner")
    x=x+1

tablelimit = 2
print(f"Only {tablelimit} can make it to dinner.")

while tablelimit < len(guest_list):
    sorrymate = guest_list.pop()
    print(f"Sorry {sorrymate} we must uninvite you as our table is too small and I am apparently too dumb or lazy to get another one in time.")

x = 0
while x < len(guest_list):
    print(f"Hello {guest_list[x]}, you are still invited to dinner")
    x=x+1

x = 0
while x < len(guest_list):
    del guest_list[x]

print(f"guest list has: {guest_list}")
