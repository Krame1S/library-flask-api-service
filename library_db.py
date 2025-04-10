import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_pass,
        host=db_host
    )
    print("Connected to the library DB!")
except psycopg2.Error as e:
    print(f"Database connection failed: {e}")
    exit(1)

try:
    cursor = conn.cursor()
    print("Cursor ready!")

    cursor.execute("""
        SELECT b.isbn, b.title, l.borrower_name, b.copies_available 
        FROM books b
        LEFT JOIN loans l ON b.isbn = l.isbn;
    """)
    books = cursor.fetchall()
    print("Books in the library:")
    for book in books:
        print(f"ISBN: {book[0]}, Title: {book[1]}, Borrower: {book[2] or 'None'}, Copies: {book[3]}")

except psycopg2.Error as e:
    print(f"Query failed: {e}")
finally:
    cursor.close()
    conn.close()
    print("Connection closed.")
