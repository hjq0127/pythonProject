"""
Replace the contents of this module docstring with your own details
Name:Hong jiaqin
Date started:26/12
GitHub URL:https://github.com/hjq0127/pythonProject/tree/main/Assessment1_fix
"""

import csv

# open the csv file
csv_file = open('book.csv', 'r')

# create the reader
csv_reader = csv.reader(csv_file, delimiter=',')

# initialize the list
books = []

# read the csv file and add to the list
for row in csv_reader:
    books.append(row)

# print welcome message
print('Welcome to the Book Tracker, created by Hong Jiaqin')

# print menu
print('Menu:')
print('L - List all books')
print('A - Add new book')
print('M - Mark a book as completed')
print('Q - Quit')

# get user input
choice = input('>>>').upper()

# loop until user chooses to quit
while choice != 'Q':
    # list all books
    if choice == 'L':
        print()
        # initialize counter
        count = 1
        # initialize page count
        page_count = 0
        # initialize required page count
        req_page_count = 0
        # initialize number of required books
        req_books = 0
        # loop through list
        for book in books:
            # if book is required
            if book[3] == 'c':
                # print required books with an asterisk
                print('*' + str(count) + '. ' + book[0] + ' by ' + book[1] + '\t\t' + book[2] + ' pages')
                # add to page count
                page_count += int(book[2])
                # add to required page count
                req_page_count += int(book[2])
                # add to number of required books
                req_books += 1
            # if book is not required
            else:
                # print completed books without an asterisk
                print(str(count) + '. ' + book[0] + ' by ' + book[1] + '\t\t' + book[2] + ' pages')
                # add to page count
                page_count += int(book[2])
            # add to counter
            count += 1
        # if there are required books
        if req_books > 0:
            # print required book and pages
            print('You need to read ' + str(req_page_count) + ' pages in ' + str(req_books) + ' books.')
    # add new book
    elif choice == 'A':
        # get title, author, and pages
        title = input('Title: ')
        author = input('Author: ')
        while True:
            try:
                pages = int(input('Pages: '))
                break
            except ValueError:
                print('Invalid input; enter a valid number.')
        # add book to list
        books.append([title, author, str(pages), 'r'])
        # print book added
        print(title + ' by ' + author + ' added!')
    # mark book as completed
    elif choice == 'M':
        # initialize count
        count = 1
        # initialize page count
        page_count = 0
        # initialize required page count
        req_page_count = 0
        # initialize number of required books
        req_books = 0
        # if there are required books
        if any('r' == book[3] for book in books):
            # loop through list
            for book in books:
                # if book is required
                if book[3] == 'c':
                    # print required books with an asterisk
                    print('*' + str(count) + '. ' + book[0] + ' by ' + book[1] + '\t\t' + book[2] + ' pages')
                    # add to page count
                    page_count += int(book[2])
                    # add to required page count
                    req_page_count += int(book[2])
                    # add to number of required books
                    req_books += 1
                # if book is not required
                else:
                    # print completed books without an asterisk
                    print(str(count) + '. ' + book[0] + ' by ' + book[1] + '\t\t' + book[2] + ' pages')
                    # add to page count
                    page_count += int(book[2])
                # add to counter
                count += 1
            # print required book and pages
            print('You need to read ' + str(req_page_count) + ' pages in ' + str(req_books) + ' books.')
            # get user choice
            while True:
                try:
                    choice = int(input('Enter the number of a book to mark as completed: '))
                    if choice < 1 or choice > len(books):
                        raise ValueError
                    break
                except ValueError:
                    print('Invalid input; enter a valid number.')
            # print book marked as completed
            if choice and 0 < int(choice) <= len(books):
                if books[choice - 1][3] == "r":
                    print(books[choice - 1][0] + ' by ' + books[choice - 1][1] + ' completed!')
                elif books[choice - 1][3] == "c":
                    print("\nThat book is already completed")
            else:
                print("\nInvalid selection.")
            # mark book as completed
            books[choice - 1][3] = 'c'
        # if there are no required books
        else:
            # print no required books message
            print('No required books!')
    else:
        # if invalid input
        print('Invalid input')
    # print menu
    print('Menu:')
    print('L - List all books')
    print('A - Add new book')
    print('M - Mark a book as completed')
    print('Q - Quit')
    # get user input
    choice = input('>>>').upper()

# open the csv file
csv_file = open('books.csv', 'w')

# create the writer
csv_writer = csv.writer(csv_file, delimiter=',')

# write to csv file
csv_writer.writerows(books)

# close the file
csv_file.close()

# print goodbye message
print('Goodbye!')
