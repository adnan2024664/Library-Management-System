class Member:
    """
    A class to represent a library member.

    Attributes:
    name : str
        The name of the member.
    borrowed_books : list
        A list of books borrowed by the member.
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the member object.

        Parameters:
        name (str): The name of the member.
        """
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Adds a book to the member's borrowed books list.

        Parameters:
        book (Book): The book to be borrowed.
        """
        self.borrowed_books.append(book)

    def return_book(self, book):
        """
        Removes a book from the member's borrowed books list.

        Parameters:
        book (Book): The book to be returned.
        """
        self.borrowed_books.remove(book)

    def __str__(self):
        """
        String representation of the member.
        """
        return f"Member Name: {self.name}"
