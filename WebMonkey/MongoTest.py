from pymongo import MongoClient
Сlient = MongoClient("10.31.1.123", 27017)
Db = Сlient.ReportsMonitoring
Collection = Db.Collection

print(Collection.find_one())
input("pause")