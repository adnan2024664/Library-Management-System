from library import Library
from book import Book
from member import Member

def main():
    library = Library()

    # Sample Data
    book1 = Book("Python 101", "John Doe")
    book2 = Book("AI for Beginners", "Jane Smith")
    library.add_book(book1)
    library.add_book(book2)

    member1 = Member("Alice")
    member2 = Member("Bob")
    library.add_member(member1)
    library.add_member(member2)

    while True:
        print("\nLibrary Management System")
        print("1. List Available Books")
        print("2. List Borrowed Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.list_available_books()
        elif choice == "2":
            library.list_borrowed_books()
        elif choice == "3":
            book_title = input("Enter the book title to borrow: ")
            member_name = input("Enter member's name: ")
            book_to_borrow = next((b for b in library.books if b.title == book_title), None)
            member = next((m for m in library.members if m.name == member_name), None)
            if book_to_borrow and member:
                library.borrow_book(book_to_borrow, member)
            else:
                print("Book or Member not found.")
        elif choice == "4":
            book_title = input("Enter the book title to return: ")
            member_name = input("Enter member's name: ")
            book_to_return = next((b for b in library.books if b.title == book_title), None)
            member = next((m for m in library.members if m.name == member_name), None)
            if book_to_return and member:
                library.return_book(book_to_return, member)
            else:
                print("Book or Member not found.")
        elif choice == "5":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
