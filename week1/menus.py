# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message
name = float(input("Enter name: "))
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = str.upper(input(">>>"))
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    name = float(input("Enter name: "))
    print("(H)ello\n(G)oodbye\n(Q)uit")




