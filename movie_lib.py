import csv
import datetime

"""
MovieLib stores the functions for calling data from the database.
"""
class MovieLib:

    def __init__(self):
        pass

    def read_from_item_file():

        with open('ml-100k/u.item', encoding='latin_1') as f:
            list_of_dicts = []
            reader = csv.DictReader(f,fieldnames=['movie_id',
                                                 'movie_title',
                                                 'date_added',
                                                 '',
                                                 'imdb_url'], delimiter='|')

            for row in reader:
                list_of_dicts.append(row)

        for dictionary in list_of_dicts:
            dictionary['movie_id'] = int(dictionary['movie_id'])
            dictionary['movie_title'] = dictionary['movie_title'][:-7]
            dictionary['genre_id'] = dictionary[None]

            for index, string in enumerate(dictionary['genre_id']):
                dictionary['genre_id'][int(index)] = int(string)

            del dictionary['']
            del dictionary[None]

        return list_of_dicts


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
