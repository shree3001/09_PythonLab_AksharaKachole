books = {
    "B1": {
        "title": "Python Basics",
        "author": "Rao",
        "copies": 2,
        "issued_to": []
    },
    "B2": {
        "title": "Data Structures",
        "author": "Iyer",
        "copies": 1,
        "issued_to": []
    },
    "B3": {
        "title": "Algorithms",
        "author": "Rao",
        "copies": 1,
        "issued_to": []
    }
}


# 1. Add Book
def add_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        copies = int(input("Enter additional copies: "))
        books[isbn]["copies"] += copies
        print("Book copies updated successfully!")

    else:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        copies = int(input("Enter number of copies: "))

        books[isbn] = {
            "title": title,
            "author": author,
            "copies": copies,
            "issued_to": []
        }

        print("Book added successfully!")


# 2. Issue Book
def issue_book():
    isbn = input("Enter ISBN: ")
    member_id = input("Enter member ID: ")

    if isbn not in books:
        print("Book not found!")
        return

    book = books[isbn]

    # Same member cannot issue the same book twice
    if member_id in book["issued_to"]:
        print("Member already holds this book!")
        return

    # Count books held by this member
    member_books = 0

    for data in books.values():
        if member_id in data["issued_to"]:
            member_books += 1

    # Maximum limit is 2 books per member
    if member_books >= 2:
        print("Member cannot hold more than 2 books!")
        return

    # Check available copies
    if book["copies"] <= 0:
        print("No copies available!")
        return

    book["copies"] -= 1
    book["issued_to"].append(member_id)

    print("Book issued successfully!")
    print("Available copies:", book["copies"])


# 3. Return Book
def return_book():
    isbn = input("Enter ISBN: ")
    member_id = input("Enter member ID: ")

    if isbn not in books:
        print("Book not found!")
        return

    book = books[isbn]

    if member_id not in book["issued_to"]:
        print("This member does not hold this book!")
        return

    book["issued_to"].remove(member_id)
    book["copies"] += 1

    print("Book returned successfully!")
    print("Available copies:", book["copies"])


# 4. Search Book
def search_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        print("\nBook Details:")
        print(books[isbn])
    else:
        print("Book not found!")


# 5. Reports
def reports():

    print("\n===== LIBRARY REPORTS =====")

    # Report 1: All books
    print("\nAll Books:")

    for isbn, book in books.items():
        print(isbn, ":", book)

    # Report 2: Books by a given author
    author_name = input("\nEnter author name: ")

    author_books = {
        isbn: book["title"]
        for isbn, book in books.items()
        if book["author"].lower() == author_name.lower()
    }

    print("\nBooks by", author_name, ":")
    print(author_books)

    # Report 3: Member -> list of books
    member_books = {}

    for isbn, book in books.items():
        for member_id in book["issued_to"]:
            member_books.setdefault(member_id, []).append(
                book["title"]
            )

    print("\nMembers Holding Books:")

    for member_id, book_list in member_books.items():
        print(member_id, ":", book_list)

    # Report 4: Members holding more than one book
    multiple_books = {
        member_id: book_list
        for member_id, book_list in member_books.items()
        if len(book_list) > 1
    }

    print("\nMembers Holding More Than One Book:")
    print(multiple_books)

    # Report 5: Books currently unavailable (0 copies)
    unavailable_books = {
        isbn: book["title"]
        for isbn, book in books.items()
        if book["copies"] == 0
    }

    print("\nUnavailable Books:")
    print(unavailable_books)

    # Report 6: Books never issued
    never_issued = {
        isbn: book["title"]
        for isbn, book in books.items()
        if len(book["issued_to"]) == 0
    }

    print("\nBooks Never Issued:")
    print(never_issued)


# Main Menu
while True:
    print("\n===== LIBRARY RECORD SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Library Record System...")
        break

    else:
        print("Invalid choice!")