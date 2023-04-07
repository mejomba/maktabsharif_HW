import datetime
from pprint import pprint

import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("localhost:27017")
db = client.library
books_collection = db['books']
users_collection = db['users']


def insert_users():
    users_collection.insert_many([
        {
            'name': 'mojtaba',
        },
        {
            'name': 'akbar',
        },
        {
            'name': 'jafar',
        }
    ])


def insert_books():
    title = input('title: ')
    if list(books_collection.find({'title': title})):
        borrowed_by = input('borrowed_by: ')
        user = users_collection.find_one({"name": borrowed_by})
        books_collection.update_one({'title': title},
                                    {'$push': {'borrowed_by': user['_id']}})
    else:
        authors = input('authors: ').split(',')
        genre = input('genres: ').split(',')
        publisher = input('publisher: ')
        isbn = int(input('isbn: '))
        description = input('description: ')
        quantity = int(input('quantity: '))
        available = int(input('available: '))
        borrowed_by = input('borrowed_by: ')
        user = users_collection.find_one({"name": borrowed_by})
        books_collection.insert_one(
            {
                'title': title,
                'author': authors,
                'genre': genre,
                'publisher': publisher,
                'publish_date': datetime.datetime.now(),
                'isbn': isbn,
                'description': description,
                'quantity': quantity,
                'available': available,
                'borrowed_by': [user['_id']]
            }
        )


def create_index_on_title():
    books_collection.create_index([('title', pymongo.ASCENDING)], unique=True)

# create_index_on_title()


def most_borrowed():
    result = books_collection.aggregate([
        {'$project': {'title': 1,
                      'publish_date': 1,
                      'number_of_borrows': {'$cond': {'if': {'$isArray': "$borrowed_by"},
                                                      'then': {'$size': "$borrowed_by"},
                                                      'else': "NA"}},
         }},
        {'$sort': {'publish_date': pymongo.ASCENDING}},
        {'$sort': {'number_of_borrows': -1}},
    ])
    for item in result:
        print(item)

# most_borrowed()

def find_by_genre():
    result = books_collection.find({
        'genre': {'$in': ['g1', 'g2']}
        # 'genre': ['g1', 'g2']
        # 'genre': 'g1'
    })
    result = books_collection.aggregate([
        {'$match': {'genre': 'g1'}},
        {'$sort': {'publish_date': pymongo.ASCENDING}}
    ])
    for item in result:
        pprint(item)

find_by_genre()

from os.path import join
import pymongo
from bson.json_util import dumps, loads


def backup_db(backup_db_dir='.'):
    client = pymongo.MongoClient("localhost:27017")
    database = client['library']

    collections = database.list_collection_names()
    print(collections)

    for i, collection_name in enumerate(collections):
        col = getattr(database, collections[i])
        collection = col.find()
        jsonpath = collection_name + ".json"
        jsonpath = join(backup_db_dir, jsonpath)
        with open(jsonpath, 'w') as jsonfile:
            for item in collection:
                jsonfile.write(dumps(item))

# backup_db()


def restore_db(restore_files):
    client = pymongo.MongoClient("localhost:27017")
    database = client['library2']

    print('inja')
    for restore_file in restore_files:
        with open(restore_file, 'r') as file:
            print(restore_file)
            data = file.read()
            load = loads(data)
            # print(load)
    # collections = database.list_collection_names()
    # print(collections)
    #
    # for i, collection_name in enumerate(collections):
    #     col = getattr(database, collections[i])
    #     collection = col.find()
    #     jsonpath = collection_name + ".json"
    #     jsonpath = join(backup_db_dir, jsonpath)
    #     with open(jsonpath, 'a+') as jsonfile:
    #         for item in collection:
    #             jsonfile.write(dumps(item))

# restore_db(['books.json', 'users.json'])
user_input = ''
while user_input != 'q':
    insert_books()
    user_input = input('q for quiet: ').lower()