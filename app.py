import database

MENU_PROMPT = """ PY BOOKS
PLEASE SELECT AN OPTION:

1. ADD NEW BOOK
2. VIEW BOOKS IN STOCK
3. SEARCH BOOK TITLE
4. SEARCH BY HIGHEST RATING
5. EXIT

SELECT: """


def menu():
    connection = database.connect()
    database.create_tables(connection)
    user_input = input(MENU_PROMPT)

    while user_input != "5":
        if user_input == "1":
            name = input("Enter book title: "),
            author = input("Enter author name: "),
            rating = int(input("Enter book rating: "))

            database.add_book(connection, name, author, rating)
        elif user_input == "2":
            books = database.get_all_books(connection)

            for book in books:
                print(book)
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Invalid entry.")


menu()
