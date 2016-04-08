"""
User stores a single row of 'u.user' data from MovieLens.
"""

class User:

    def __init__(self, dictionary):

        self.id = int(dictionary['user_id'])
        self.age = int(dictionary['age'])
        self.gender = dictionary['gender']
        self.occupation = dictionary['occupation']
        self.zip_code = dictionary['zip_code']
