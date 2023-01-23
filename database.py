from pymongo import MongoClient
from models import Blog
# connection = MongoClient("mongodb+srv://sayali:sayali@decimalpoint.fnk8t.mongodb.net/?retryWrites=true&w=majority")


client = MongoClient("mongodb+srv://sayali:sayali@decimalpoint.fnk8t.mongodb.net/?retryWrites=true&w=majority")
database = client.fastapi
collection = database.blogs

