from django.db import models
from pymongo import MongoClient
from django.conf import settings

# Create your models here.

client = MongoClient(settings.MONGODB_URI)
db = client['bookgraphql']

class BookDocument:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def save(self):
        db.books.insert_one({'title': self.title, 'author': self.author})