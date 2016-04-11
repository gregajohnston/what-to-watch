import csv
import math
from rating import Rating

NUMBER_OF_USERS = 943

"""
RatingLib stores a list of Rating items.
"""
class RatingLib:

    def __init__(self, list_of_ratings = []):
        self.list_of_ratings = list_of_ratings


    def read_from_data_file(self):
        self.list_of_ratings = []

        with open('ml-100k/u.data', encoding='latin_1') as f:
            reader = csv.DictReader(f,fieldnames=['user_id',
                                                 'item_id',
                                                 'rating',
                                                 'timestamp'], delimiter='\t')

            for row in reader:
                self.list_of_ratings.append(Rating(row))

        return self.list_of_ratings


    def find_all_ratings_objects_by_movie_id(self, lookup_id):
        return_list = []

        for rating_obj in self.list_of_ratings:
            if rating_obj.movie_id == lookup_id:
                return_list.append(rating_obj)

        return return_list


    def find_all_ratings_objects_by_user_id(self, lookup_id):
        return_list = []

        for rating_obj in self.list_of_ratings:
            if rating_obj.user_id == lookup_id:
                return_list.append(rating_obj)

        return return_list


    def find_average_rating_value_from_list(self, ratings_list):
        if len(ratings_list) == 0:
            return 0
        numbers_list = []

        for rating_obj in ratings_list:
            numbers_list.append(rating_obj.rating)

        return sum(numbers_list)/len(numbers_list)


    def euclidean_distance(self, v, w):
        if len(v) is 0:
            return 0

        differences = [v[idx] - w[idx] for idx in range(len(v))]
        squares = [diff ** 2 for diff in differences]
        sum_of_squares = sum(squares)

        return 1 / (1+ math.sqrt(sum_of_squares))

    def is_user_match_helper(self, lookup_id_one, lookup_id_two):
        list_one = self.find_all_ratings_objects_by_user_id(lookup_id_one)
        list_one.sort(key=lambda x: x.movie_id, reverse=True)
        list_two = self.find_all_ratings_objects_by_user_id(lookup_id_two)
        list_two.sort(key=lambda x: x.movie_id, reverse=True)
        list_one_ids = set(x.movie_id for x in list_one)
        list_two_ids = set(x.movie_id for x in list_two)

        inter_one = [item for item in list_one
                            if item.movie_id in list_two_ids]
        inter_two = [item for item in list_two
                            if item.movie_id in list_one_ids]

        return inter_one, inter_two, lookup_id_two

    def is_user_match(self, list_one, list_two, lookup_id_two):

        inter_one, inter_two, lookup_id_two = is_user_match_helper(lookup_id_one, lookup_id_two)

        pass_one, pass_two = [], []
        for item in inter_one:
            pass_one.append(item.rating)
        for item in inter_two:
            pass_two.append(item.rating)

        return self.euclidean_distance(pass_one, pass_two), lookup_id_two


    def find_best_user_match(self, lookup_id):

        match_value, match_user = 0, 0
        temp_value, temp_user = 0, 0

        for number in range(1, NUMBER_OF_USERS + 1):
             temp_value, temp_user = self.is_user_match(lookup_id, number)
             if temp_value > match_value:
                 match_value, match_user = temp_value, temp_user

        return match_value, match_user
