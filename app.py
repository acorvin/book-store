import database

MENU_PROMPT = """ ***** PY BOOKS *****
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

    while True:
        user_input = input(MENU_PROMPT)

        if user_input == "1":
            name = input("Enter book title: ")
            author = input("Enter author name: ")
            rating = int(input("Enter book rating: "))

            database.add_book(connection, name, author, rating)
            break
        elif user_input == "2":
            books = database.get_all_books(connection)

            for book in books:
                print(f"{book[1]} by {book[2]} - Rating: {book[3]}")
        elif user_input == "3":
            name = input("Enter book title: ")
            books = database.get_books_by_name(connection, name)

            for book in books:
                print(f"{book[1]} ({book[2]} - {book[3]}")
        elif user_input == "4":
            name = input("Enter the book name: ")
            highest_rating = database.get_best_rated_books(connection, name)

            print(f"Highest Rated: {name} - Rating: {highest_rating[3]}")
        elif user_input == "5":
            break
        else:
            print("Invalid entry")


menu()
