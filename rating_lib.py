
import csv
from rating import Rating

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
