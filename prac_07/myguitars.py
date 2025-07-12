from prac_07.guitar import Guitar
import csv

def main():
    """The main program is used for managing guitar collections"""
    guitars = load_guitars()

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

    add_new_guitars(guitars)
    guitars.sort()
    save_guitars(guitars)
    print("Guitars saved to file.")


def load_guitars():
    """Load data from csv"""

def add_new_guitars(guitars):
    """Add a new guitar based on user input"""

def save_guitars(guitars):
    """save"""

main()

