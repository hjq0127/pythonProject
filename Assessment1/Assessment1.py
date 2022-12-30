"""
Replace the contents of this module docstring with your own details
Name:Hong jiaqin
Date started:26/12
GitHub URL:https://github.com/JCUS-CP1404/cp1404-reading-tracker---assignment-1-hjq0127.git
"""
import csv

csvfile = open('book.csv', 'r')
data = list(csv.reader(csvfile))
i = 0
print("Reading Tracker 1.0 - by Hong jiaqin")

total = 0
for row in data:
    if row[3] == 'r':
        total += int(row[2])

# load csv (book file)
with open('book.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    books = []
    for row in csv_reader:
        books.append(row)

# looping menu
while True:
    print("\nMenu:")
    print("L. List Books")
    print("A. Add Book")
    print("M. Mark Book as Complete")
    print("Q. Quit")
    option = input("\nSelect an Option: ").upper()

    # list books
    if option == 'L':
        print("\nBook List:")
        if len(books) == 0:
            print("No Books.")
        else:
            # sort books by author and then title
            for i, book in enumerate(books):
                if book[3] == "c":
                    print("*""{}. {} by {} ({} pages; {})".format(i + 1, book[0], book[1], book[2], book[3]))
                else:
                    print("{}. {} by {} ({} pages; {})".format(i + 1, book[0], book[1], book[2], book[3]))
        print("You need to read ", total, " pages in ", i + 1, "books")


    # add book
    elif option == 'A':
        title = input("\nEnter book title: ")
        author = input("Enter book author: ")
        pages = input("Enter number of pages: ")
        # error checking
        while True:
            if pages.isdigit() and int(pages) > 0:
                books.append([title, author, pages, "required"])
                print("\nBook added.")
                break
            elif pages.isdigit() <= 0:
                print("Number must be > 0")
                pages = input("Enter number of pages: ")
            else:
                print("\nInvalid page number.")
                pages = input("Enter number of pages: ")
                books.append([title, author, pages, "required"])

    # mark book as complete
    elif option == 'M':
        print("\nBook List:")
        if len(books) == 0:
            print("No Books.")
        else:
            # sort books by author and then title
            for i, book in enumerate(books):
                if book[3] == "c":
                    print("*""{}. {} by {} ({} pages; {})".format(i + 1, book[0], book[1], book[2], book[3]))
                else:
                    print("{}. {} by {} ({} pages; {})".format(i + 1, book[0], book[1], book[2], book[3]))
            book_num = input("\nSelect a book: ")
            # error checking
            if book_num.isdigit() and 0 < int(book_num) <= len(books):
                if books[int(book_num) - 1][3] == "r":
                    books[int(book_num) - 1][3] == "c"
                    print(book[1], "completed!")
                else:
                    print("\nThat book is already completed")
            else:
                print("\nInvalid selection.")

    # exit
    elif option == 'Q':
        # save book to csv
        with open('books.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            for book in books:
                csv_writer.writerow(book)
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid menu choice")



