import pymongo
client = pymongo.MongoClient("mongodb+srv://Prashikgole:maruti7609@cluster07.3ohjsfu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"prashik",
    "email":"gole.prashik@gmail.com",
    "surname" :"gole"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)