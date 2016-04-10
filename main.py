from movie_lib import MovieLib

def print_welcome():
    print("Welcome to GREGFLIX")

def initialize_database():
    movie_library = MovieLib().read_from_item_file()
    user_library = UserLib().read_from_user_file()
    rating_library = RatingLib().read_from_data_file()

def find_all_ratings_for_movie(lookup_id, rating_lib):
    return_list = []
    for rating_obj in rating_lib:
        if rating_obj.movie_id == lookup_id:
            return_list.append(rating_obj.rating)
    return return_list

def find_average_ratings_for_movie(lookup_id, rating_lib):
    return_list = find_all_ratings_for_movie(lookup_id, rating_lib)
    return sum(return_list)/len(return_list)

def find_name_for_movie(lookup_number):
    pass

def find_all_ratings_for_user(lookup_number):
    pass

def main():
    #print_welcome()
    #initialize_database()
    pass




if __name__ == '__main__':
    main()
