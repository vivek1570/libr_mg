from book import Book

def add_book():
    book_name=input(f"Enter the name of the book?")
    book_author=input(f"Enter the author of the book?")
    book_year=input(f"Enter the year of the book?")
    objBook=Book()
    objBook.add_book(book_name,book_author,book_year)
def view_books():
    objBook=Book()
    objBook.view_books()
def issue_book():
    pass

def return_book():
    pass

def search_book():
    pass
    

def main_menu():
    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            search_book()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

main_menu()