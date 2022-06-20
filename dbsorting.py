# sort elements alphabetically in ascending order

import pymongo

# establish connection
# to the database
my_client = pymongo.MongoClient('localhost', 27017)

mydb = my_client["python"]

mynew = mydb["table"]

rec = {
    '_id': 1,
    'language':'java',
    'database': 'mongodb',
    'code editor': "eclipse"
}

# sorting function
mydb = mynew.find().sort("language")

for x in mydb:
    print(x)