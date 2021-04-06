from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]
mycol = mydb["startup_log"]

mydict = {"name": "John1", "address": "Highway 317"}

x = mycol.insert_one(mydict)
