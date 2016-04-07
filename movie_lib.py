import csv

"""
MovieLib stores the functions for calling data from the database.
"""
class MovieLib:

    def __init__(self):
        pass

    def read_from_item_file():

        with open('ml-100k/u.item', encoding='latin_1') as f:
            return_dict = {}
            reader = csv.DictReader(f,
                                    fieldnames=['movie_id',
                                                'movie_title',
                                                '',
                                                '',
                                                'genre_id'], delimiter='|')

            for row in reader:
                return_dict.update({'movie_id': row['movie_id'],
                                    'movie_title': row['movie_title'],
                                    'genre_id': row['genre_id']})

        return return_dict


# def main():
#     pass

# if __init__ == '__main__':
#     main()

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
