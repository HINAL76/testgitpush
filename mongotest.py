import pymongo
client = pymongo.MongoClient("mongodb+srv://Hinal:Hinal07@cluster0.brroq8f.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name":"Hinal",
    "email":"hinal18@gmail.com",
    "surnmae": "parikh",
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

