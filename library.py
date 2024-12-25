from book import Book
from member import Member

class Library:
    """
    A class which represents the library.

    Attributes:
    - books (list): A list of books within the library.
    - members (list): A list of members within the library.
    """

    def __init__(self):
        """
        respresnts a library method with empty book and member list.
        """
        self.books = []
        self.members = []

    def add_book(self, book):
        """
        includes a book to the library.

        Args:
        - book (Book): The book that will be added.
        """
        self.books.append(book)

    def remove_book(self, book):
        """
        Removes a book from the library.

        Args:
        - book (Book): The book that will be removed.
        """
        if book in self.books:
            self.books.remove(book)

    def add_member(self, member):
        """
        includes a member to the library.

        Args:
        - member (Member): The member that will be added.
        """
        self.members.append(member)

    def remove_member(self, member):
        """
        Removes a member from the library 

        Args:
        - member (Member): The member that will be removed.
        """
        if member in self.members:
            self.members.remove(member)

    def borrow_book(self, book, member):
        """
        permits  a memeber to borrow a book from the library.

        Args:
        - book (Book): The book to borrow form the library.
        - member (Member): The member who is borrowing the book.
        """
        if book in self.books:
            self.books.remove(book)
            member.borrow_book(book)
            print(f"{member.name} borrowed {book}.")
        else:
            print(f"The book {book} is not available.")

    def return_book(self, book, member):
        """
        permits the return of a book to the library by a member.

        Args:
        - book (Book): The book to be returned to the library.
        - member (Member): The member that is returning the book.
        """
        if book in member.borrowed_books:  
          member.return_book(book)       
          self.books.append(book)        
        else:
          print(f"Error: Member '{member.name}' has not borrowed the book '{book.title}'.")

    def list_available_books(self):
        """
       lists every book that is available in the library.
        """
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    def list_borrowed_books(self):
        """
        Lists all the books that have been borrowed and who has borrowed. 
        """
        print("\nBorrowed Books:")
        for member in self.members:
            for book in member.borrowed_books:
                print(f"{book} - Borrowed by {member.name}")
