"""
Rating stores a single row of 'u.data' from MovieLens.
"""

class Rating:

    def __init__(self, dictionary):

        self.user_id = int(dictionary['user_id'])
        self.movie_id = int(dictionary['item_id'])
        self.rating = int(dictionary['rating'])
        self.timestamp = int(dictionary['timestamp'])
