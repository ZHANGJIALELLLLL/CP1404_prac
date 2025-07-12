from prac_07.project import Project
def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    menu_choice = ""
    while menu_choice.upper() != "Q":
        display_menu()
        menu_choice = input(">>> ").upper()

        if menu_choice == "L":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif menu_choice == "S":
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects_by_date(projects)
        elif menu_choice == "A":
            add_new_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        elif menu_choice == "Q":
            if input("Would you like to save to projects.txt? ").lower().startswith("y"):
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid menu choice")

def display_menu():
    """menu"""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    """Load projects from file."""

def save_projects(filename, projects):
    """Save projects to file"""

def display_projects(projects):
    """display projects"""

def filter_projects_by_date(projects):
    """Filter and display projects that start after a specified date"""

def add_new_project(projects):
    """Add a new project from user input"""

def update_project(projects):
    """Update"""


main()