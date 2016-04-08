from movie import Movie
from movie_lib import MovieLib
from user import User
from user_lib import UserLib
from nose.tools import raises

mov_lib = MovieLib
def test_read_from_item_file():
    """read_from_item_file takes no input, but reads from the csv file named
    'u.item' in the MovieLens database and returns a list"""
    assert type(mov_lib.read_from_item_file()) == list


def test_formate_from_item_file():
    """instead of strings, format the various dictionary values into types
    based on the data in them"""
    assert mov_lib.read_from_item_file()[0].id == 1
    assert mov_lib.read_from_item_file()[0].genre[0] == 0


u_lib = UserLib
def test_read_from_user_file():
    """read_from_item_file takes no input, but reads from the csv file named
    'u.user' in the MovieLens database and returns a list"""
    assert type(u_lib.read_from_item_file()) == list

def test_format_from_user_file():
    """read_from_item_file takes no input, but reads from the csv file named
    'u.user' in the MovieLens database and returns a list"""
    assert u_lib.read_from_item_file()[0].id == 1
    assert u_lib.read_from_item_file()[0].genre[0] == 0
