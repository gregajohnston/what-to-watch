
import csv
from rating import Rating

"""
RatingLib stores a list of Rating items.
"""
class RatingLib:

    def __init__(self):
        self.list_of_ratings = []

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
