"""
Movies stores a single row of 'u.item' data from MovieLens.
"""


class Movie:

    def __init__(self, dictionary):

        self.id = int(dictionary['movie_id'])
        self.title = dictionary['movie_title'][:-7]
        self.genre = []
        for item in dictionary[None]:
            self.genre.append(int(item))

        del dictionary['']
        del dictionary[None]

        # self.movie_item = {'movie_id': self.id,
        #                     'movie_title': self.title,
        #                     'genre': self.genre}
