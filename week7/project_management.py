"""
CP1404/CP5632 Practical
Project Management Program
"""
import csv

# Create a Project class to store the project data
class Project:
    def __init__(self, name, start_date, end_date, completion, priority):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.completion = completion
        self.priority = priority


# Function to load projects from the data file
def load_projects(filename):
    projects = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                project = Project(*row)
                projects.append(project)
    return projects


# Function to save projects to the data file
def save_projects(filename, projects):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for project in projects:
            writer.writerow([project.name, project.start_date, project.end_date, project.completion, project.priority])


# Function to display projects
def display_projects(projects):
    print("Incomplete projects:")
    print("Name\tStart Date\tEnd Date\tCompletion\tPriority")
    incomplete_projects = [project for project in projects if project.completion != 100]
    incomplete_projects.sort(key=lambda x: x.priority, reverse=True)
    for project in incomplete_projects:
        print(f"{project.name}\t{project.start_date}\t{project.end_date}\t{project.completion}\t{project.priority}")

    print("\nCompleted projects:")
    print("Name\tStart Date\tEnd Date\tCompletion\tPriority")
    complete_projects = [project for project in projects if project.completion == 100]
    complete_projects.sort(key=lambda x: x.priority, reverse=True)
    for project in complete_projects:
        print(f"{project.name}\t{project.start_date}\t{project.end_date}\t{project.completion}\t{project.priority}")


# Function to filter projects by date
def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > date]
    filtered_projects.sort(key=lambda x: x.start_date)
    for project in filtered_projects:
        print(f"{project.name}\t{project.start_date}\t{project.end_date}\t{project.completion}\t{project.priority}")


# Function to add a new project
def add_project(projects):
    name = input("Name: ")
    start_date = input("Start date: ")
    end_date = input("End date: ")
    completion = input("Completion percentage: ")
    priority = input("Priority: ")
    project = Project(name, start_date, end_date, completion, priority)
    projects.append(project)


# Function to update a project
def update_project(projects):
    name = input("Name of the project to update: ")
    for project in projects:
        if project.name == name:
            completion = input("New completion percentage (leave blank to retain existing value): ")
            if completion:
                project.completion = completion
            priority = input("New priority (leave blank to retain existing value): ")
            if priority:
                project.priority = priority


# Main program
filename = input("Enter the filename to load/save projects: ")
projects = load_projects(filename)

# Display menu
while True:
    print("\nMenu:")
    print("1. Load projects")
    print("2. Save projects")
    print("3. Display projects")
    print("4. Filter projects by date")
    print("5. Add new project")
    print("6. Update project")
    print("7. Quit")
    selection = input("Enter your selection: ")

    # Load projects
    if selection == "1":
        projects = load_projects(filename)
    # Save projects
    elif selection == "2":
        save_projects(filename, projects)
    # Display projects
    elif selection == "3":
        display_projects(projects)
    # Filter projects by date
    elif selection == "4":
        date = input("Enter date (YYYY-MM-DD): ")
        filter_projects_by_date(projects, date)
    # Add new project
    elif selection == "5":
        add_project(projects)
    # Update project
    elif selection == "6":
        update_project(projects)
    # Quit
    elif selection == "7":
        save_projects(filename, projects)
        break
    else:
        print("Invalid selection. Please try again.")