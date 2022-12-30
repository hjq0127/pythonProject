"""
Replace the contents of this module docstring with your own details
Name:Hong jiaqin
Date started:26/12
GitHub URL:
"""

#Reading Tracker 1.0 - by Lindsay Ward

#importing the csv module
import csv

#A function to read the books from the CSV file and add them to the books list
def read_csv():
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for book in reader:
            #adding the books to the books list
            books.append(book)

#A function to write the books from the books list to the CSV file
def write_csv():
    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)

#A function to add a new book to the books list
def add_book():
    title = input("Title: ")
    #Error-checking the title
    while title == '':
        print("Input can not be blank")
        title = input("Title: ")
    author = input("Author: ")
    #Error-checking the author
    while author == '':
        print("Input can not be blank")
        author = input("Author: ")
    #Error-checking the pages
    while True:
        try:
            pages = int(input("Pages: "))
            if pages <= 0:
                print("Number must be > 0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    #Adding the new book to the books list
    book = [title, author, pages, 'r']
    books.append(book)
    print(f"{title} by {author}, ({pages} pages) added to Reading Tracker")

#A function to mark a book as completed
def mark_complete():
    #Displaying the list of books
    print("You need to read", total_pages, "pages in", total_required, "books.")
    i = 1
    for book in books:
        if book[3] == 'r':
            print(f"*{i}. {book[0]} by {book[1]}\t\t{book[2]} pages")
        else:
            print(f" {i}. {book[0]} by {book[1]}\t\t{book[2]} pages")
        i += 1
    #Error-checking the book number
    while True:
        try:
            book_num = int(input("Enter the number of a book to mark as completed: "))
            if book_num <= 0 or book_num > len(books):
                print("Invalid book number")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    #Marking the book as completed
    books[book_num - 1][3] = 'c'

#A function to calculate the total pages and total required books
def calculate_total():
    global total_pages
    global total_required
    total_pages = 0
    total_required = 0
    for book in books:
        total_pages += int(book[2])
        if book[3] == 'r':
            total_required += 1

#Main program
print("Reading Tracker 1.0 - by Lindsay Ward")
#An empty list to store the books
books = []
#Reading the books from the CSV file
read_csv()
#Calculating the total pages and total required books
calculate_total()
#Displaying the number of books loaded
print(len(books), "books loaded")
#Looping menu
while True:
    print("Menu:")
    print("L - List all books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")
    choice = input(">>> ").upper()
    #List all books
    if choice == 'L':
        i = 1
        for book in books:
            if book[3] == 'r':
                print(f"*{i}. {book[0]} by {book[1]}\t\t{book[2]} pages")
            else:
                print(f" {i}. {book[0]} by {book[1]}\t\t{book[2]} pages")
            i += 1
        if total_required == 0:
            print("No required books!")
        else:
            print("You need to read", total_pages, "pages in", total_required, "books.")
    #Add new book
    elif choice == 'A':
        add_book()
    #Mark a book as completed
    elif choice == 'M':
        if total_required != 0:
            mark_complete()
        else:
            print("No required books!")
    #Quit
    elif choice == 'Q':
        write_csv()
        break
    #Invalid menu choice
    else:
        print("Invalid menu choice")