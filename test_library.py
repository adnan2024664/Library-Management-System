"""
Test cases for the Library Management System.
"""

from library import Library
from book import Book
from member import Member

# Test for adding book to the Library
def test_add_books():
    
    #add books to the library 
    print("--------Testing adding books to the Library.----------")
    library = Library()
    first_book = Book("Charlie and Chocolate Factory", "Roald Dahl")
    second_book = Book("I am rebel ", "Ross Montgomery")
    #adding firstbook
    library.add_book(first_book)
    #adding secondbook 
    library.add_book(second_book)

    # confirm the books were added 
    assert first_book in library.books, "The first_book was not added to the Library system."
    assert second_book in library.books, "The second_book was not added to the Library stystem. "
    # if successful  print: 
    print("Books have been successfully added to the Library!\n")


# adding members to the library
def test_add_members():
    
    print("-------Testing for adding members to the Library----------")
    library = Library()
    member1 = Member("Jackie")
    member2 = Member("John")
    #add member!
    library.add_member(member1)
    #add member2
    library.add_member(member2)

    # confirm the members were added
    assert member1 in library.members, "Member1 has not been added to the library system."
    assert member2 in library.members, "Member2 has not been added to the library system."
    # successful message: 
    print("The members have been added to the Library!\n")


# test for borrowing a book from the Library 
def test_borrow_book():
   
    print("---------Testing borrowing a book from the Library-----------")
    library = Library()
    book = Book("1I am Rebel", "Ross Montgomery")
    member = Member("John")
    library.add_book(book)
    library.add_member(member)

    # Function to borrow the book
    library.borrow_book(book, member)

    # verify that the book has been borrowed from the system 
    assert book not in library.books, "book shoud not be in the Library."
    assert book in member.borrowed_books, "Book should be in the member's borrowed books list."
    print("The book has been borrowed!\n")

# test for returning the book to the Library
def test_return_book():

    print("---------Testing returning a book to the Library-----------")
    library = Library()
    book = Book("Charlie and Chocolate Factory", "Roald Dahl")
    member = Member("John")
    library.add_book(book)
    library.add_member(member)

    # Functions to first borrow book 
    library.borrow_book(book, member)
    # then returns the book 
    library.return_book(book, member)

    # verify if the book has been returned to the Library
    assert book in library.books, "Book should be put back into the Library."
    assert book not in member.borrowed_books, "Book has been taken out of the member's borrowed list."
    print("Book has been successfully returned to the Library!\n")


#run all of the tests 
def run_tests():

    print("......Running the following tests for the Library Management System.....\n")
    #test for adding book 
    test_add_books()
    #tets to add member
    test_add_members()
    #tests to borrow a book 
    test_borrow_book()
    #tests to return book 
    test_return_book()

    
    print("All the tests have been completed!")

#run the tests as outputs 
if __name__ == "__main__":
    run_tests()
