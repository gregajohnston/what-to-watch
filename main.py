from movie_lib import MovieLib
from user_lib import UserLib
from rating_lib import RatingLib
from print_handler import PrintHandler

NUMBER_OF_MOVIES = 1682


def initialize_database():

    movie_library = MovieLib()
    movie_library.list_of_movies = MovieLib().read_from_item_file()
    user_library = UserLib()
    user_library.list_of_users = UserLib().read_from_user_file()
    rating_library = RatingLib()
    rating_library.list_of_ratings = RatingLib().read_from_data_file()

    temp_list = []
    for movie in movie_library.list_of_movies:
        temp_list = rating_library.find_all_ratings_objects_by_movie_id(
                                                            movie.movie_id)
        movie.average_rating = rating_library.find_average_rating_value_from_list(temp_list)
        movie.rating_count = len(temp_list)

    return movie_library, user_library, rating_library


def find_best_rated_user_not_seen(lookup_id, rating_lib, movie_lib,
                                    times_rated_threshold, return_count):

    list_of_user_ratings = rating_lib.find_all_ratings_objects_by_user_id(
                                                                lookup_id)

    check_list = []
    for rating_obj in list_of_user_ratings:
        check_list.append(rating_obj.movie_id)

    return_list = []
    for movie_obj in movie_lib.list_of_movies:
        if movie_obj.movie_id not in check_list:
            return_list.append(movie_obj)

    return MovieLib(return_list).find_best_rated_movies(
                                    times_rated_threshold,
                                    return_count)


def main():

    PrintHandler.print_welcome()
    movie_library, user_library, rating_library = initialize_database()
    PrintHandler.print_user_options()

    while True:

        user_input = input("> ")
        if type(user_input) == str:
            if user_input.lower() == 'compare':
                user_input = input("Enter a user number\n> ")
                mv, mu = rating_library.find_best_user_match(user_input)
                print('similarity: {}, user: {}'.format(mv, mu))
                continue
            if user_input.lower() == 'quit':
                print("Exiting the program.")
                break

        try:
            user_input = int(user_input)
        except ValueError:
            print("Not a number")
            continue

        if user_input == 0:
            PrintHandler.print_top_ten()
            return_list = movie_library.find_best_rated_movies(50, 10)
            for item in return_list:
                print(item)

        elif user_input >= 1 and user_input <= 943:
            PrintHandler.print_your_top_ten()
            return_list = find_best_rated_user_not_seen(user_input,
                                        rating_library, movie_library, 50 ,10)

            for item in return_list:
                print(item)

        else:
            print("Please choose a number between 0 and 943.")


if __name__ == '__main__':
    main()
