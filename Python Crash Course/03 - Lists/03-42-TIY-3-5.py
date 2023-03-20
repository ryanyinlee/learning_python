#3-5 changing guest list

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

