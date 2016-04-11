from nose.tools import raises

from user import User
from user_lib import UserLib

from movie import Movie
from movie_lib import MovieLib

from rating import Rating
from rating_lib import RatingLib

from main import *


mov_lib = MovieLib()
mov_lib.list_of_movies = MovieLib().read_from_item_file()
m = mov_lib.list_of_movies[0]
def test_read_from_item_file():
    """read_from_item_file takes no argument, but parses the 'u_item'
    file and returns a list of items"""
    assert type(mov_lib.list_of_movies) == list

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

rate_lib = RatingLib()
rate_lib.list_of_ratings = RatingLib().read_from_data_file()
rate = rate_lib.list_of_ratings[0]
def test_read_from_data_file():
    """read_from_user_file takes no argument, but parses the 'u_data'
    file and returns a list of users"""
    assert type(rate_lib) == type(RatingLib())
    assert type(rate) == type(Rating({'user_id':1,
                                    'item_id':1, 'rating':1, 'timestamp':1}))

def test_format_data_object():
    """after reading the file, each rating object is a formatted based on
    the type of entry"""
    assert rate.user_id == 196
    assert rate.movie_id == 242
    assert rate.rating == 3


test_case_one = rate_lib.find_all_ratings_objects_by_movie_id(1)
def test_find_all_ratings_objects_by_movie_id():
    assert type(test_case_one) == list
    assert test_case_one[1].rating == 5
    assert test_case_one[10].rating == 5


test_case_two = rate_lib.find_average_rating_value_from_list(test_case_one)
def test_find_average_rating_value_from_list():
    assert type(test_case_two) == float
    assert test_case_two >= 0 and test_case_two <= 5

def test_find_title_string_for_movie():
    assert type(mov_lib.find_title_string_for_movie(1)) == str

def find_all_ratings_objects_by_user_id():
    assert type(rate_lib.find_all_ratings_objects_by_user_id(1)) == list
