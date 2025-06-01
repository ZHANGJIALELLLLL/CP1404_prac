def main():
    """Get the score and display the status"""
    score = float(input("Enter score: "))
    print(score_status(score))

def score_status(score):
    if score < 0 or score > 1000:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
main()

