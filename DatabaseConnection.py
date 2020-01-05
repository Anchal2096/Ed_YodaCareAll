from pymongo import MongoClient
from DefaultDatabaseValues import *
client = MongoClient("localhost", 27017)

# used database
db = client["EDYODA_CAREALL"]

Elders_Table = db["old_people_collection"]
Elders_Table.insert_many(Elders_Table_List)
YoungFolks_Table = db["young_people_collection"]

YoungFolks_Table.insert_many(YoungFolks_List)

# print(client.list_database_names())
