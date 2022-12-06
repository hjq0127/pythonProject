"""
CP1404/CP5632 Practical
Email to name dictionary
"""


# Create an empty dictionary
user_dict = {}

# Prompt user to enter an email
email = input("Please enter your email: ")

# Loop until the user enters a blank email
while email != "":

    # Extract name from email
    name = email.split("@")[0].title().split(".")
    name = " ".join(name)

    # Check if name is correct
    check_name = input("Is your name {}? (Y/n): ".format(name))

    # If name is not correct, ask user to enter their name
    if check_name.lower() != "y":
        name = input("Please enter your name: ")

    # Store user's email and name in dictionary
    user_dict[email] = name

    # Prompt user to enter another email
    email = input("Please enter your email: ")

# Loop through the dictionary and print users' emails and names
for email, name in user_dict.items():
    print("Email: {}\tName: {}".format(email, name))