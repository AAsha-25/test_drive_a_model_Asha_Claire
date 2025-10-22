from lib.album import Album

"""
Album constructs with an id, title and release_year
"""
def test_album_constructs():
    album = Album(1, "Dark Side", "1995", 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == "1995"
    assert album.artist_id == 2

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Dark Side", "1995", "1")
    assert str(album) == "Album(1, Dark Side, 1995, 1)"
    # Try commenting out the `__repr__` method in lib/album.py
    # And see what happens when you run this test again.

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Dark Side", "1995", "2")
    album2 = Album(1, "Dark Side", "1995", "2")
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/album.py
    # And see what happens when you run this test again.


"""
Constructs with 
    id, title, release_year, and artist_id
"""
def test_construsts_with_fields():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.artist_id == 2

