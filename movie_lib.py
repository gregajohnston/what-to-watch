import csv
import datetime
from movie import Movie


"""
MovieLib stores a list of Movie items.
"""
class MovieLib:

    def __init__(self):
        pass

    def read_from_item_file():

        with open('ml-100k/u.item', encoding='latin_1') as f:
            list_of_movies = []
            reader = csv.DictReader(f,fieldnames=['movie_id',
                                                 'movie_title',
                                                 'date_added',
                                                 '',
                                                 'imdb_url'], delimiter='|')

            for row in reader:
                list_of_movies.append(Movie(row))

        

        return list_of_movies


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
