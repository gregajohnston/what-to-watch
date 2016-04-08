import csv
import datetime
from movie import Movie

"""
MovieLib stores a list of Movie items.
"""
class MovieLib:

    def __init__(self):
        self.list_of_movies = []

    def read_from_item_file(self):
        self.list_of_movies = []
        with open('ml-100k/u.item', encoding='latin_1') as f:
            reader = csv.DictReader(f,fieldnames=['movie_id',
                                                 'movie_title',
                                                 'date_added',
                                                 '',
                                                 'imdb_url'], delimiter='|')

            for row in reader:
                self.list_of_movies.append(Movie(row))

        return self.list_of_movies
