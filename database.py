import sqlite3

# Query
CREATE_BOOKS_TABLE = "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, name TEXT, author TEXT, rating INTEGER);"
INSERT_BOOK = "INSERT INTO books (name, author, rating) VALUES (?, ?, ?);"
GET_ALL_BOOKS = "SELECT * FROM books;"
GET_BOOKS_BY_NAME = "SELECT * FROM books WHERE name = ?;"
GET_BEST_RATED_BOOKS = """
SELECT * FROM books
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""


# Create the sqlite3 database if it does not exist
def connect():
    return sqlite3.connect("data.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_BOOKS_TABLE)


# receive the data from the user
def add_book(connection, name, author, rating):
    with connection:
        connection.execute(INSERT_BOOK, (name, author, rating))


# Get books
def get_all_books(connection):
    with connection:
        return connection.execute(GET_ALL_BOOKS).fetchall()  # fetchall = get list of rows returned by database


def get_books_by_name(connection, name):
    with connection:
        return connection.execute(GET_BOOKS_BY_NAME, (name,)).fetchall()


def get_best_rated_books(connection, name):
    with connection:
        return connection.execute(GET_BEST_RATED_BOOKS, (name,)).fetchone()  # fetchone = returns one row (rating)
