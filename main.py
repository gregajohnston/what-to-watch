from movie_lib import MovieLib

NUMBER_OF_MOVIES = 1682

def print_welcome():
    print("Welcome to GREGFLIX")

def initialize_database():
    movie_library = MovieLib().read_from_item_file()
    user_library = UserLib().read_from_user_file()
    rating_library = RatingLib().read_from_data_file()

def find_all_ratings_objects_by_movie_id(lookup_id, rating_lib):
    return_list = []
    for rating_obj in rating_lib:
        if rating_obj.movie_id == lookup_id:
            return_list.append(rating_obj)
    return return_list
#returns list of rating objects with movie.id==lookup_id

def find_average_rating_value_by_movie_id(ratings_list):
    if len(ratings_list) == 0:
        return 0

    numbers_list = []
    for rating_obj in ratings_list:
        numbers_list.append(rating_obj.rating)

    return sum(numbers_list)/len(numbers_list)
#returns single number, sum of ratings / count of ratings

def find_title_string_for_movie(lookup_id, movie_lib):
    return [movie_obj.title for movie_obj in movie_lib
                    if movie_obj.movie_id == lookup_id][0]
# returns string of movie title for movie_id==lookup_id

def find_all_ratings_for_user(lookup_id, rating_lib):
    return_list = []
    for rating_obj in rating_lib:
        if rating_obj.user_id == lookup_id:
            return_list.append(rating_obj)
    return return_list
#returns list of rating objects with user.id==lookup_id

def return_most_popular_movies_helper(rating_lib, NUMBER_OF_MOVIES):
    return_list = []
    for number in range(1, NUMBER_OF_MOVIES+1):
        return_list.append(
                    [find_average_ratings_for_movie(
                        find_average_ratings_for_movie(number, rating_lib)),
                        number])
    return return_list

def getKey(item):
    return item[0]

def return_most_popular_movies(rating_lib, movie_lib):
    print("Here are the 20 most highly rated movies (minumum 10 ratings):")
    start_list = return_most_popular_movies_helper(rating_lib, NUMBER_OF_MOVIES)
    start_list.sort(key=getKey, reverse=True)
    return_list = start_list[:20]
    for value in return_list:
        value[1] = find_name_for_movie(value[1], movie_lib)

    return return_list

def return_only_ten_plus_ratings(rating_lib):
    return_lib = []
    for number in range(1, NUMBER_OF_MOVIES+1):
        temp_list = find_all_ratings_objects_by_movie_id(number, rating_lib)
        if len(temp_list) >= 10:
            return_lib.append(temp_list)
    return return_lib




def main():
    #print_welcome()
    #initialize_database()
    pass




if __name__ == '__main__':
    main()
