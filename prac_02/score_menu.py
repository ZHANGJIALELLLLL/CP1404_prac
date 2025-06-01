def main():
    score = 0 #Initialization
    menu_choice = ""  #Initialization
    while menu_choice != "Q":
        print("\nMenu:")
        print("(G) Get a new valid score")
        print("(P) Print result")
        print("(S) Show stars")
        print("(Q) Quit")

        menu_choice = input(">>>").upper()
        if menu_choice == "G":
            score = get_valid_score()
        elif menu_choice == "P":
            print(score_status(score))
        elif menu_choice == "S":
            show_start(score)
        elif menu_choice == "Q":
            print("Thank you!")
        else:
            print("invalid choice")

def get_valid_score():
    score = float(input("Enter score(0-100): "))
    while score < 0 or score > 1000:
        print("Score must be between 0 and 100.")
        score = float(input("Enter score(0-100): "))
    return score

def score_status(score):
    if score < 0 or score > 1000:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_start(score):
    """Print start *"""
    print("*" * int(score))

main()