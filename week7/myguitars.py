"""
CP1404/CP5632 Practical
Guitars class with tests.
"""


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost


guitar_list = []

# Read data from file
with open("guitars.csv") as file:
    for line in file:
        data = line.strip().split(',')
        name = data[0]
        year = data[1]
        cost = data[2]
        guitar_list.append(Guitar(name, year, cost))

# Display the data
for guitar in guitar_list:
    print("Guitar Name: {}, Year: {}, Cost: ${}".format(guitar.name, guitar.year, guitar.cost))
