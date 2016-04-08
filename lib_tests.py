from user import User
from user_lib import UserLib
from movie import Movie
from movie_lib import MovieLib
from nose.tools import raises


mov_lib = MovieLib().read_from_item_file()
m = mov_lib[0]
def test_read_from_item_file():
    """read_from_item_file takes no argument, but parses the 'u_item'
    file and returns a list of items"""
    assert type(mov_lib) == list

def test_format_movie_object():
    """after reading the file, each movie object is a formatted based on
    the type of entry"""
    assert m.id == 1
    assert m.title == "Toy Story"


user_lib = UserLib().read_from_user_file()
u = user_lib[0]
def test_read_from_user_file():
    """read_from_user_file takes no argument, but parses the 'u_user'
    file and returns a list of users"""
    assert type(user_lib) == list

def test_format_user_object():
    """after reading the file, each user object is a formatted based on
    the type of entry"""
    assert u.id == 1
    assert u.gender == "M"
