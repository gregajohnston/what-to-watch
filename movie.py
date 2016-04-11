"""
Movies stores a single row of 'u.item' from MovieLens.
"""

class Movie:

    def __init__(self, dictionary):

        self.movie_id = int(dictionary['movie_id'])
        self.title = dictionary['movie_title'][:-7]
        self.genre = []
        for item in dictionary[None]:
            self.genre.append(int(item))

        del dictionary['']
        del dictionary[None]

        self.average_rating = -1
        self.rating_count = -1
