class Member:
    """
    A class to represent a library member.

    Attributes:
    name : str  The name of the member.
    borrowed_books : list
        A list of books borrowed by the member.
    """

    def __init__(self, name):
        """
        formats a member with name and empty borrowed book list 

        args:
        name (str): The name of the member.
        """
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        This adds a book to the member's borrowed books list.

        args:
        book (Book): The book to be borrowed.
        """
        self.borrowed_books.append(book)

    def return_book(self, book):
        """
        This takes a book away from the member's borrowed books list.

        args:
        book (Book): The book to be returned.
        """
        if book in self.borrowed_books:
           self.borrowed_books.remove(book)
           print(f"Book '{book.title}' returned successfully.")
        else:
           print(f"Error: The book '{book.title}' is not in the borrowed list.")

    def __str__(self):
        """
        symbolises string of the member.
        """
        return f"Member Name: {self.name}"
