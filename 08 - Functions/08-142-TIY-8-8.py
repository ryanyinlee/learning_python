#8-8 user albums

def make_album():
    """Takes in artist and album name to return a dictionary of this info"""
    
    print(f"Let's input an album!")
    print(f"\nType 'Q' to quit at anytime.")

    while True:
        artist_name = input(f"Please enter the artist name:")
        if artist_name.lower() == 'q':
            break
        album_title = input(f"Please enter the album title:")
        if album_title.lower() == 'q':
            break
        numsongs = input(f"Please enter how many songs are in the album")
        if numsongs.lower == 'q':
            break
        album = {'Artist': {artist_name}, 'Album': {album_title}, 'No. of Songs': {numsongs}}
        print(album)

make_album()