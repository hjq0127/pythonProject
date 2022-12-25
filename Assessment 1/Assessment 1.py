# Welcome to the Book List Program!
# I'm [Name] and I will be guiding you through the program.

# Load CSV file
import csv

# Create book list
book_list = []


# Create function to read from csv file
def read_csv_file():
    with open('book_list.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            book_list.append(line)


# Create function to print book list
def print_book_list():
    print('Here is your book list:')
    for book in book_list:
        print(f'{book[0]}, by {book[1]}, pages: {book[2]}')


# Create function to add book
def add_book():
    title = input('Please enter the title of the book you would like to add: ')
    author = input('Please enter the author of the book you would like to add: ')
    pages = input('Please enter the number of pages in the book you would like to add: ')
    book_list.append([title, author, pages])
    if pages < 0:
        print("Invalid pages number")


# Create function to mark book as complete
def mark_complete():
    if len(book_list) < 0:
        print('No books required!')
    elif len(book_list) > 0:
        print('Please enter the number of the book you have completed: ')
        for index, book in enumerate(book_list):
            print(f'{index + 1}. {book[0]}')
        choice = input()
        if type(input) != int:
            print('Invalid input')
        book_list.pop(choice - 1)
    else:
        print("Invalid input")


# Create function to save book list to csv file
def save_book_list():
    with open('book_list.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for book in book_list:
            csv_writer.writerow(book)


# Main program
def main():
    # Read CSV file
    read_csv_file()

    # Display circular menu
    while True:
        print('What would you like to do?')
        print('L. List Books')
        print('A. Add Book')
        print('M. Mark Book as Complete')
        print('Q. Quit')
        choice = (input(">>>").upper())
        if choice == "L":
            print_book_list()
        elif choice == "A":
            add_book()
        elif choice == "M":
            mark_complete()
        elif choice == "Q":
            save_book_list()
            print(len(book_list), "books saved to books.csv")
            exit()
        else:
            print('Invalid menu choice')


# Call main function
if __name__ == '__main__':
    main()
