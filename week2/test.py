import random

low = int(input("Enter your low number:"))
high = int(input("Enter your high number:"))
while low > high:
    print("low > high please enter again")
    low = int(input("Enter your low number:"))
    high = int(input("Enter your high number:"))
else:
    print("your low number is:", low, "your high number is", high)

smiley_face_number = random.randrange(low, high)
print(":)" * smiley_face_number)


