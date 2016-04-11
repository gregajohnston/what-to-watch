from movie_lib import MovieLib
from user_lib import UserLib
from rating_lib import RatingLib
from search_handler import SearchHandler


NUMBER_OF_MOVIES = 1682

def print_welcome():
    print("Welcome to GREGFLIX")


def find_best_rated_user_not_seen(lookup_id,
                                    rating_lib,
                                    movie_lib,
                                    times_rated_threshold,
                                    return_count):

    list_of_user_ratings = find_all_ratings_objects_by_user_id(lookup_id,
                                                                rating_lib)
    check_list = []
    for rating_obj in list_of_user_ratings:
        check_list.append(rating_obj.movie_id)

    return_list = []
    for movie_obj in movie_lib:
        if movie_obj.movie_id not in check_list:
            return_list.append(movie_obj)

    return find_best_rated_movies(return_list,
                                    times_rated_threshold,
                                    return_count)


def initialize_database():
    movie_library = MovieLib().read_from_item_file()
    user_library = UserLib().read_from_user_file()
    rating_library = RatingLib().read_from_data_file()
    temp_list = []
    for movie in movie_library:
        temp_list = rating_library.find_all_ratings_objects_by_movie_id(
                                                            movie.movie_id)
        movie.average_rating = find_average_rating_value_from_list(temp_list)
        movie.rating_count = len(temp_list)
    del temp_list[:]










def main():
    print_welcome()
    initialize_database()





if __name__ == '__main__':
    main()
