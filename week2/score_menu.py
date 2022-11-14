import random
MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            mark = random.randrange(0, 100)
            print(mark)
        elif choice == "P":
            score_status = determine_score(score)
            print(score_status)
        elif choice == "S":
            print(score * '*')
        else:
            print("farewell")


def determine_score(score):
    if score < 0 or score > 100:
        score_status = "Invalid score"
    elif score >= 90:
        score_status = "Excellent"
    elif score >= 50:
        score_status = "Passable"
    else:
        score_status = "Bad"
    return score_status


main()
