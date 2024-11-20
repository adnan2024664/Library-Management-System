'''
    Test Classes and Methods here
'''

from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember

def create_instance():
    # Create a new instance of the Book class
    try:
        book = Book("Eloquent Python", "Abdulhameed")
        print(f"New instance of Book class created: {book.title} by {book.author}")
    except NameError as e:
        print(f"Error creating Book instance: {e}")

    # Create a new instance of the Library class
    try:
        library = Library()
        print("New Library instance created")
    except NameError as e:
        print(e)

    # Create a new instance of the Member class
    try:
       member = Member("Jack")
       print(f"New Member instance created: {member.name}")
    except NameError as e:
        print(e)

    # Create a new instance of the TeacherMember class
    try:
        teacher = TeacherMember("Mr. Bob", "T001")
        print(f"New TeacherMember instance created: {teacher.name}, ID: {teacher.teacher_id}")
    except NameError as e:
        print(e)


    return 



'''
Library Operations
'''
def test_library_operations():
#cretaed a library insatnce 

  library = Library()

 # create a book instances 
  book1 = Book("Eloquent Python", "Abdulhameed")
  book2 = Book("1984", "George Orwell")

# Add books to the library
  library.add_book(book1)
  library.add_book(book2)
  print("\nBooks added to the library:")
  library.list_available_books()

# Create member instances
  student = StudentMember("Alice", "S001")
  teacher = TeacherMember("Mr. Bob", "T002")

# Add member to the library
  library.add_member(student)
  library.add_member(teacher)
  print("\nMembers added to the library:")


# List available books in the library
  library.list_available_books()

# Borrow a book from the library
  print("\nBorrowing a book:")
  library.borrow_book(book1, student)
  print(f"Books currently borrowed by {student.name}: {[book.title for book in student.borrowed_books]}")


# List borrowed books from the library
  print("\nListing borrowed books:")
  library.list_borrowed_books()

