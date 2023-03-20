from name_function import get_formatted_name

print('Enter Q to quit')

while True:
    first = input("\nFirst name: ")
    if first.lower() == 'q':
        break
    last = input('\nLast name: ')
    if last.lower() == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly Named: {formatted_name}")