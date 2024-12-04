import unittest
from book import Book
from library import Library
from member import Member

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        """Setup objects for testing."""
        self.library = Library()
        self.book1 = Book("Python 101", "John Doe")
        self.book2 = Book("AI for Beginners", "Jane Smith")
        self.member1 = Member("Alice")
        self.member2 = Member("Bob")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_member(self.member1)
        self.library.add_member(self.member2)

    def test_add_book(self):
        """Test adding a book to the library."""
        new_book = Book("Data Science", "Jane Doe")
        self.library.add_book(new_book)
        self.assertIn(new_book, self.library.books)

    def test_remove_book(self):
        """Test removing a book from the library."""
        self.library.remove_book(self.book1)
        self.assertNotIn(self.book1, self.library.books)

    def test_borrow_book(self):
        """Test borrowing a book."""
        self.library.borrow_book(self.book1, self.member1)
        self.assertNotIn(self.book1, self.library.books)
        self.assertIn(self.book1, self.member1.borrowed_books)

    def test_return_book(self):
        """Test returning a book."""
        self.library.borrow_book(self.book1, self.member1)
        self.library.return_book(self.book1, self.member1)
        self.assertIn(self.book1, self.library.books)
        self.assertNotIn(self.book1, self.member1.borrowed_books)

    def test_list_available_books(self):
        """Test listing available books."""
        self.library.borrow_book(self.book1, self.member1)
        available_books = [book.title for book in self.library.books]
        self.assertNotIn(self.book1.title, available_books)

    def test_list_borrowed_books(self):
        """Test listing borrowed books."""
        self.library.borrow_book(self.book1, self.member1)
        borrowed_books = [book.title for book in self.member1.borrowed_books]
        self.assertIn(self.book1.title, borrowed_books)

if __name__ == "__main__":
    unittest.main()
