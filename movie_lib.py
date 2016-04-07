"""
MovieLib stores the functions for calling data from the database.
"""
import csv

class MovieLib:
    def __init__(self):
        pass


    def read_from_item_file():

        with open('ml-100k/u.item', encoding='latin_1') as f:
            return_dict = {}
            reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', '', '', 'something_else'], delimiter='|')

            for row in reader:
                return_dict.update({'movid_id': row['movie_id'],
                                    'movie_title': row['movie_title'],
                                    'something_else': row['something_else']})
            print(type(return_dict))
            return return_dict
#
#
# with open('another.csv') as f:
#     reader = csv.DictReader(f, delimiter="\t")
#     for row in reader:
#         print(row)
#


# with open('something.csv') as f:
#     reader = f.reader(f)
#     headers = next(reader)
#     print(headers)
#     print('-------')
#     for row in reader:
#         print(row)
#
# with open('something.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(reader)
#
# with open('another.csv') as f:
#     reader = csv.DictReader(f, delimiter="\t")
#     for row in reader:
#         print(row)
#
