"""
Movie stores an instance of the MovieLens data.
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
