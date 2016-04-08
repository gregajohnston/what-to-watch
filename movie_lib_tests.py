from movie_lib import MovieLib
from nose.tools import raises

mov_lib = MovieLib
def test_read_from_item_file():
    """read_from_item_file takes no input, but reads from the csv file named
    'u.item' in the MovieLens database and returns a dictionary"""
    assert type(mov_lib.read_from_item_file()) == list
    assert type(mov_lib.read_from_item_file()[0]) == dict

def test_formate_from_item_file():
    """instead of strings, format the various dictionary values into types
    based on the data in them"""
    assert mov_lib.read_from_item_file()[0]['movie_id'] == 1
    assert mov_lib.read_from_item_file()[0]['genre_id'][0] == 0
