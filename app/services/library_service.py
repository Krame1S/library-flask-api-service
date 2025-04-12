from app.db import db

def get_books():
    books = db.get_all_books()
    return books