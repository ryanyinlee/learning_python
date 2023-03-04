glossary = {
    'dictionary': 'an object with key value pairs',
    'variable': 'a thing what stored that can be changed',
    'tuple': 'an immutable variable',
    'if': 'check if something',
    'in': 'check if in something',
    'list': 'list of things',
    'comments': 'used to make notes in code',
    'string': 'sequence of characters',
    'boolean': 'true or false',
    'operators': 'stuff that lets you do math'

}

for term, definition in glossary.items():
    print(f"Term: {term.title()} \n Definition: {definition.title()}")