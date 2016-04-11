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




    def find_title_string_for_movie(self, lookup_id):
        for movie_obj in self.list_of_movies:
            if movie_obj.movie_id == lookup_id:
                return movie_obj.title
    

    def find_best_rated_movies(self, times_rated_threshold, return_count):
        return_list = []
        for movie in self.list_of_movies:
            if movie.rating_count >= times_rated_threshold:
                return_list.append(movie)
        return_list.sort(key=lambda x: x.average_rating, reverse=True)
        return return_list[:return_count]
