from book import Book
from member import Member

class Library:
    """
    Represents a library.

    Attributes:
    - books (list): A list of books in the library.
    - members (list): A list of members in the library.
    """

    def __init__(self):
        """
        Initializes an empty library.
        """
        self.books = []
        self.members = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
        - book (Book): The book to be added.
        """
        self.books.append(book)

    def remove_book(self, book):
        """
        Removes a book from the library.

        Args:
        - book (Book): The book to be removed.
        """
        if book in self.books:
            self.books.remove(book)

    def add_member(self, member):
        """
        Adds a member to the library.

        Args:
        - member (Member): The member to be added.
        """
        self.members.append(member)

    def remove_member(self, member):
        """
        Removes a member from the library.

        Args:
        - member (Member): The member to be removed.
        """
        if member in self.members:
            self.members.remove(member)

    def borrow_book(self, book, member):
        """
        Allows a member to borrow a book from the library.

        Args:
        - book (Book): The book to be borrowed.
        - member (Member): The member borrowing the book.
        """
        if book in self.books:
            self.books.remove(book)
            member.borrow_book(book)
            print(f"{member.name} borrowed {book}.")
        else:
            print(f"The book {book} is not available.")

    def return_book(self, book, member):
        """
        Allows a member to return a book to the library.

        Args:
        - book (Book): The book to be returned.
        - member (Member): The member returning the book.
        """
        self.books.append(book)
        member.return_book(book)
        print(f"{member.name} returned {book}.")

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    def list_borrowed_books(self):
        """
        Lists all borrowed books and their borrowers.
        """
        print("\nBorrowed Books:")
        for member in self.members:
            for book in member.borrowed_books:
                print(f"{book} - Borrowed by {member.name}")