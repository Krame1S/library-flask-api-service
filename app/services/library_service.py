from app.db import db

def get_books():
    books = db.get_all_books()
    return books

def create_book(isbn, title, copies_available):
    if not isbn or not title:
        raise ValueError("ISBN and title are required")
    if len(title) > 30:
        raise ValueError("Title must be 30 characters or less")
    if copies_available < 0:
        raise ValueError("Copies available cannot be negative")
    if not isbn.isdigit() or len(isbn) != 13:
        raise ValueError("ISBN must be 13 digits")
    db.add_book(isbn, title, copies_available)

def update_book(isbn, title, copies_available):
    if not isbn or not title:
        raise ValueError("ISBN and title are required")
    if len (title) > 30:
        raise ValueError("Title must be 30 chars or less")
    if copies_available < 0:
        raise ValueError("Copies cannot be negative")
    if not isbn.isdigit() or len(isbn) != 13:
        raise ValueError("ISBN must be 13 digits")
    db.update_book(isbn, title, copies_available)    

def delete_book(isbn):
    if not isbn:
        raise ValueError("ISBN is required")
    if not isbn.isdigit() or len(isbn) != 13:
        raise ValueError("ISBN must be 13 digits")
    db.delete_book(isbn)
