#8-7 album

def make_album(artist_name, album_title, num_songs=None):
    """Takes in artist and album name to return a dictionary of this info"""
    album = {'Artist': artist_name, 'Album': album_title}
    if num_songs:
        album['No. of Songs'] = num_songs
    return album

album1 = make_album("Deftones", "Defjammin")

album2 = make_album("Dry Eras4e", "The Board", 16)

print(album1)

print(album2)