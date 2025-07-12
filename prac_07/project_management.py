import datetime
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
    projects = []
    try:
        with open(filename, 'r') as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found")
    return projects


def save_projects(filename, projects):
    """Save projects to file"""
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """display projects"""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete_projects):
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter and display projects that start after a specified date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [p for p in projects if p.start_date > filter_date]
        for project in sorted(filtered_projects, key=attrgetter('start_date')):
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy")

def add_new_project(projects):
    """Add a new project from user input"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")

    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    print(f"{name} added.")

def update_project(projects):
    """Update"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)

        new_percentage = input("New Percentage: ")
        if new_percentage:
            project.completion_percentage = int(new_percentage)

        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid project selection")


main()