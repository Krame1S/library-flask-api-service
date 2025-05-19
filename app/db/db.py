import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST")
    )
    return conn

def get_all_books():
    conn = get_db_connection() 
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.isbn, b.title, l.borrower_name, b.copies_available
        FROM books b
        LEFT JOIN loans l ON b.isbn = l.isbn;
    """)
    books = cursor.fetchall()
    cursor.close()
    conn.close()

    result = []
    for book in books:
        books_dict = {'isbn': book[0], 'title': book[1], 'borrower': book[2], 'copies': book[3]}
        if books_dict['borrower'] is None:
            books_dict['borrower'] = 'None'
        result.append(books_dict)

    return result

def add_book(isbn, title, copies_available):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (isbn, title, copies_available) 
        VALUES (%s, %s, %s);
    """, (isbn, title, copies_available))
    conn.commit()
    cursor.close()
    conn.close()

def update_book(isbn, title, copies_available):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books
        SET title = %s, copies_available = %s
        WHERE isbn = %s;
    """, (title, copies_available, isbn))
    conn.commit()
    cursor.close()
    conn.close()

def delete_book(isbn):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE isbn = %s;", (isbn,))
    conn.commit()
    cursor.close()
    conn.close()