class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Member:
    def __init__(self, name):
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.book_list = []
        self.member_list = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        book = Book(title, author)
        self.book_list.append(book)
        print("Book added successfully.")

    def add_member(self):
        name = input("Enter member name: ")
        member = Member(name)
        self.member_list.append(member)
        print("Member added.")

    def lend_book(self):
        name = input("Enter member name: ")
        title = input("Enter book title: ")

        for member in self.member_list:
            if member.name == name:
                for book in self.book_list:
                    if book.title == title:
                        member.books.append(book)
                        self.book_list.remove(book)
                        print("Book issued.")
                        return
        print("Book or Member not found.")

    def return_book(self):
        name = input("Enter member name: ")
        title = input("Enter book title: ")

        for member in self.member_list:
            if member.name == name:
                for book in member.books:
                    if book.title == title:
                        self.book_list.append(book)
                        member.books.remove(book)
                        print("Book returned.")
                        return
        print("Book not found.")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.book_list:
            print(book.title, "-", book.author)


# Menu Driven Program
library = Library()

while True:
    print("\n1.Add Book")
    print("2.Add Member")
    print("3.Lend Book")
    print("4.Return Book")
    print("5.Display Books")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.add_member()
    elif choice == 3:
        library.lend_book()
    elif choice == 4:
        library.return_book()
    elif choice == 5:
        library.display_books()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")