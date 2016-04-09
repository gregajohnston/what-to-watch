from nose.tools import raises

from user import User
from user_lib import UserLib

from movie import Movie
from movie_lib import MovieLib

from rating import Rating
from rating_lib import RatingLib

mov_lib = MovieLib().read_from_item_file()
m = mov_lib[0]
def test_read_from_item_file():
    """read_from_item_file takes no argument, but parses the 'u_item'
    file and returns a list of items"""
    assert type(mov_lib) == list

def test_format_movie_object():
    """after reading the file, each movie object is a formatted based on
    the type of entry"""
    assert m.movie_id == 1
    assert m.title == "Toy Story"


user_lib = UserLib().read_from_user_file()
user = user_lib[0]
def test_read_from_user_file():
    """read_from_user_file takes no argument, but parses the 'u_user'
    file and returns a list of users"""
    assert type(user_lib) == list

def test_format_user_object():
    """after reading the file, each user object is a formatted based on
    the type of entry"""
    assert user.user_id == 1
    assert user.gender == "M"

rate_lib = RatingLib().read_from_data_file()
rate = rate_lib[0]
def test_read_from_data_file():
    """read_from_user_file takes no argument, but parses the 'u_data'
    file and returns a list of users"""
    assert type(rate_lib) == list

def test_format_data_object():
    """after reading the file, each rating object is a formatted based on
    the type of entry"""
    assert rate.user_id == 196
    assert rate.movie_id == 242
    assert rate.rating == 3


def test_find_all_ratings_movie():
    pass
#    assert type(find_all_ratings_for_movie(1)) == list

def test_find_average_ratings_movie():
    pass
#    assert type(find_average_ratings_for_movie(1)) == float

def test_find_name_movie():
    pass
#    assert type(find_name_for_movie(1)) == str

def test_find_all_ratings_user():
    pass
#    assert type(find_all_ratings_for_user(1)) == list
