#import the these classes form the other files in LibraryManagementSystem
from library import Library
from book import Book
from member import Member

def main():
    library = Library()

    #add books to the library 
    book1 = Book("Charlie and Chocolate Factory", "Roald Dahl")
    book2 = Book("I am rebel ", "Ross Montgomery")
    #add book1 to the library 
    library.add_book(book1)
    #add book2 to the library 
    library.add_book(book2)
    
    #initialise a memmebr to the book. member1 and member2 creates the name of members 
    member1 = Member("Jackie")
    member2 = Member("Josh")
    #add member1 to the library
    library.add_member(member1)
    #add memeber2 to the libraray 
    library.add_member(member2)


    while True:
        #prints the options for user to select
        print("\nLibrary Programme ")
        print("Please select an option from below:")
        print("1. List Available Books")
        print("2. List Borrowed Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        #This intialises the users choice 
        choice = input("Enter your choice: ")
         
        # List the available books for user
        if choice == "1":
            library.list_available_books()

        # list the borrowed boook for the user 
        elif choice == "2":
            library.list_borrowed_books()
        
        # Functions for user to borrow book from the library
        elif choice == "3":
            # enter the name of the book 
            book_title = input("Enter the title of the book you want to borrow: ")
            # enter member name in the library 
            member_name = input("Enter the name of member please: ")
            # Look in the ystem to find the book and member 
            book_to_borrow = next((b for b in library.books if b.title == book_title), None)
            member = next((m for m in library.members if m.name == member_name), None)
            # If the book and member is correct, borrow the book
            if book_to_borrow and member:
                library.borrow_book(book_to_borrow, member)
            # if not found in the system, display not found. 
            else:
                print("Book or Member not found. Please try again!")


        # Functions to return book to the library system
        elif choice == "4":
            # user input for name of book 
            book_title = input("Enter the title of the book you want to return: ").strip()
            # user input for memeber name 
            member_name = input("Enter the name of the member : ").strip()

            #look for the book and member for returning to the library
            member = next((m for m in library.members if m.name.lower() == member_name.lower()), None)

            # If member has not been found, display error message
            if not member:
               print(f"Error: Member '{member_name}' not found.")
            else: 
               book_to_return = next((b for b in member.borrowed_books if b.title.lower() == book_title.lower()), None)
               
              # when book is not found, display the message as follows: 
               if not book_to_return:
                print(f"Invalid: The member '{member_name}' has not borrowed the book '{book_title}'.")

               else:
                # return to user with succseful message when book is returned 
                library.return_book(book_to_return, member)
                print(f"Book '{book_title}' has been returned by {member_name}.")
            

        # functions to exit the system 
        elif choice == "5":
            print("Goodbye! You have exited the Library programme")
            break
        # manages the wrong inputs 
        else:
            print("Error. Please select a option from 1 to 5. ")

# This feature makes sure that the main function only executes when this file is run directly.
if __name__ == "__main__":
    main()
