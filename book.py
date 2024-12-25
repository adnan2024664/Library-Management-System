class Book:
    """
    A class wcich represents a book within the libary.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    """

    def __init__(self, title, author):
        """
       gives the book object a title and an author 

        args:
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
