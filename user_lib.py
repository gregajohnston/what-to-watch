import csv
from user import User

"""
UserLib stores a list of User items.
"""
class UserLib:

    def __init__(self):
        self.list_of_users = []

    def read_from_user_file(self):
        self.list_of_users = []
        with open('ml-100k/u.user', encoding='latin_1') as f:
            reader = csv.DictReader(f,fieldnames=['user_id',
                                                 'age',
                                                 'gender',
                                                 'occupation',
                                                 'zip_code'], delimiter='|')

            for row in reader:
                self.list_of_users.append(User(row))

        return self.list_of_users
