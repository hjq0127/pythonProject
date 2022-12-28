"""
CP1404/CP5632 Practical
Project Management Program
"""
import csv

# Create a Project class to store the project data
import datetime

import csv

# Main Function
def main():
    projects = []
    while True:
        print("Project Management System")
        print("L. Load Project")
        print("S. Save Project")
        print("D. Display projects")
        print("F. Filter by Date")
        print("A. Add New Item")
        print("U. Update Project")
        print("Q. Exit")
        try:
            choice = input("Enter your choice: ").upper()
            if choice == "L":
                projects = load_project()
            elif choice == "s":
                save_project(projects)
            elif choice == "D":
                display_projects(projects)
            elif choice == "F":
                projects = filter_by_date(projects)
            elif choice == "A":
                projects = add_new_item(projects)
            elif choice == "U":
                projects = update_project(projects)
            elif choice == "Q":
                break
        except:
            print("Invalid choice. Try again.")

# Load Project
def load_project():
    filename = input("Enter the filename to load: ")
    try:
        with open(filename) as f:
            lines = f.readlines()
            projects = []
            for line in lines[1:]:
                data = line.strip().split("\t")
                projects.append(projects(*data))
            return projects
    except:
        print("Error loading file.")
        return []

# Save Project
def save_project(projects):
    filename = input("Enter the filename to save: ")
    try:
        with open(filename, "w") as f:
            f.write("Name\tStart Date\tPercent Complete\tPriority\n")
            for project in projects:
                f.write("{}\t{}\t{}\t{}\n".format(project.name, project.start_date, project.percent_complete, project.priority))
    except:
        print("Error saving file.")

# Showcase Projects
def display_projects(projects):
    unfinished = []
    completed = []
    for project in projects:
        if project.percent_complete < 100:
            unfinished.append(project)
        else:
            completed.append(project)
    print("Unfinished Projects:")
    for project in sorted(unfinished, key=lambda x: x.priority):
        print("{} - {}".format(project.name, project.priority))
    print("Completed Projects:")
    for project in sorted(completed, key=lambda x: x.priority):
        print("{} - {}".format(project.name, project.priority))

# Filter by Date
def filter_by_date(projects):
    date = input("Enter date (MM/DD/YYYY): ")
    try:
        dt = datetime.datetime.strptime(date, "%m/%d/%Y")
        filtered_projects = [p for p in projects if p.start_date > dt]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print("{} - {}".format(project.name, project.start_date))
        return filtered_projects
    except:
        print("Invalid date.")
        return projects

# Add New Item
def add_new_item(projects):
    name = input("Enter project name: ")
    start_date = input("Enter start date (MM/DD/YYYY): ")
    percent_complete = input("Enter percent complete: ")
    priority = input("Enter priority: ")
    try:
        dt = datetime.datetime.strptime(start_date, "%m/%d/%Y")
        projects.append(projects(name, dt, percent_complete, priority))
        return projects
    except:
        print("Invalid date.")
        return projects

# Update Project
def update_project(projects):
    for i, project in enumerate(projects):
        print("{}. {}".format(i+1, project.name))
    try:
        choice = int(input("Enter the number of the project you want to update: "))
        project = projects[choice-1]
        percent_complete = input("Enter new percent complete (leave blank to retain existing): ")
        priority = input("Enter new priority (leave blank to retain existing): ")
        if percent_complete:
            project.percent_complete = percent_complete
        if priority:
            project.priority = priority
        return projects
    except:
        print("Invalid choice.")
        return projects


if __name__ == "__main__":
    main()