class Book:
    """
    A class to represent a book.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    """

    def __init__(self, title, author):
        """
        Constructs all the necessary attributes for the book object.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of the book.
        """
        return f"'{self.title}' by {self.author}"
