class Book:
    def __init__(self, author, title, price, publisher, stock):
        self.author = author
        self.title = title
        self.price = price
        self.publisher = publisher
        self.stock = stock

    def display(self):
        print("Author:", self.author)
        print("Title:", self.title)
        print("Price:", self.price)
        print("Publisher:", self.publisher)
        print("Stock:", self.stock)


# creating book list (inventory)
books = [
    Book("R.K. Narayan", "Malgudi Days", 300, "ABC Publisher", 10),
    Book("Chetan Bhagat", "Half Girlfriend", 250, "XYZ Publisher", 5),
    Book("APJ Abdul Kalam", "Wings of Fire", 350, "Universities Press", 8)
]

# taking input from customer
title = input("Enter book title: ")
author = input("Enter author name: ")

found = False

for book in books:
    if book.title == title and book.author == author:
        found = True
        print("\nBook Available")
        book.display()

        copies = int(input("Enter number of copies required: "))

        if copies <= book.stock:
            total_cost = copies * book.price
            print("Total Cost:", total_cost)
            book.stock -= copies
        else:
            print("Required number of copies are not available")

if not found:
    print("Book not available in inventory")