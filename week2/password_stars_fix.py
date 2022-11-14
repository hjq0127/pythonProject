minmum_leght = 4
def password_1():
    password = input(f"Enter password of at least{minmum_leght} characters:")
    while len(password) < minmum_leght:
        password = input(f"Enter password of at least {minmum_leght} characters: ")

    print('*' * len(password))

def get_password(minimum_length):
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password

def main():
    password = get_password(minmum_leght)
    print_asterisks(password)

def print_asterisks(sequence):
    print('*' * len(sequence))


main()