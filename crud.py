from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client ['python']

coll = db['table']

rec = {
    'language':'python',
    'database': 'mongodb',
    'code editor': "vscode"
}

recone = db.table.insert_one(rec)