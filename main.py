# this is the main file where i run all the cli commands
# i import argparse for the cli and my own files for the data, remember the coorect import structure
# this is the key and crucial partttttt
#import argparse first remember thats key then import thhe rest of files
#rememer to add -- to run well like in canvas

#lemme write a checklist
# step 1, I  import argparse and my files
# atep 2, write add_user function. this is for adding new users except from the one in data.json
# step 3: write list_users function, for listing the users
# atwp 4, write add_project function for adding new users then lter i put for projects
# step 5: write list_projects function same as users for listing projects
# STEP 6: write add_task function, for adding new utasks
# STEP 7: write list_tasks function for listinh yasks
# STEP 8: write complete_task function for when tasks are completed without pending part
# STEP 9: set up argparse at the bottom. very keyyy.

#step uno
import argparse
from userfile import User
from project import Project
from task import Task
from persistencefile import load_data, save_data

#step 2for addiing user
# this function adds a new user
# load the data first, then create a dictionary for the new user
# append it to the users list, save it and print a success message
def add_user(args):
    data = load_data()
    new_user = {"name": args.name, "email": args.email, "projects": []}
    data["users"].append(new_user)
    save_data(data)
    print(f"this user {args.name} has been added successfully. congrattssss.")

#step 3 for listing the users
# this function lists all users
# load the data, then loop through the users list and print each one i can use for in loop
def list_users(args):
    data = load_data()
    print("Users")
    for user in data["users"]:
        print(f"user name is: {user['name']}and his/her  email: {user['email']}")

#step 4 for adding projects
# this function adds a new project, this should be easy i use sam eway i did for listing
# load the data, create a dictionary for the new project, append and save. walaa.
def add_project(args):
    data = load_data()
    new_project = {"title": args.title, "description": args.description, "due_date": args.due_date, "owner": args.user, "tasks": []}
    data["projects"].append(new_project)
    save_data(data)
    print(f"this project {args.title} has been added to systema")

#step 5 for listing the projects
# this function lists all projects
# load the data, loop through projects and print each one use for loops
def list_projects(args):
    data = load_data()
    print("Projects")
    for project in data["projects"]:
        print(f"title: {project['title']}  owner: {project['owner']} is due: {project['due_date']}")

#step 6 for adding tasks
# this function adds a new task
# load the data, create a dictionary for the new task with status pending, append and save
def add_task(args):
    data = load_data()
    new_task = {"title": args.title, "assigned_to": args.assigned_to, "status": "pending", "project": args.project}
    data["tasks"].append(new_task)
    save_data(data)
    print(f"this specific task {args.title} has been added to system")

#step 7 for listing taks
# this function lists all tasks
# load the data, loop through tasks and print each one
def list_tasks(args):
    data = load_data()
    print("Tasks")
    for task in data["tasks"]:
        print(f"title: {task['title']} which was assigned to: {task['assigned_to']} and its status: {task['status']}")

#step 8 for marking complete atsks
# this function marks a task as complete
# load the data, loop through tasks, find the matching one and change status to complete
def complete_task(args):
    data = load_data()
    for task in data["tasks"]:
        if task["title"] == args.title:
            task["status"] = "complete"
            save_data(data)
            print(f"this task {args.title} is complete fully, congrats")
            return
    print(f"task {args.title} was not found please try again or add the task")


# this is where i set up argparse - very key!
# i create the main parser then add subparsers for each command
# each command has its arguments and is connected to its function
#i also set defaults
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    # add-user command - needs a name and email
    parser_add_user = subparsers.add_parser("add-user", help="add a new user")
    parser_add_user.add_argument("--name", required=True, help="user name")
    parser_add_user.add_argument("--email", required=True, help="user email")
    parser_add_user.set_defaults(func=add_user)

    # list-users command - no arguments needed just lists everyone
    parser_list_users = subparsers.add_parser("list-users", help="list all users")
    parser_list_users.set_defaults(func=list_users)

    # add-project command - needs a user, title, description and due date
    parser_add_project = subparsers.add_parser("add-project", help="add a new project")
    parser_add_project.add_argument("--user", required=True, help="owner of the project")
    parser_add_project.add_argument("--title", required=True, help="project title")
    parser_add_project.add_argument("--description", default="no description", help="project description")
    parser_add_project.add_argument("--due-date", dest="due_date", default="no due date", help="due date")
    parser_add_project.set_defaults(func=add_project)

    # list-projects command - no arguments needed just lists all projects
    parser_list_projects = subparsers.add_parser("list-projects", help="list all projects")
    parser_list_projects.set_defaults(func=list_projects)

    # add-task command - needs a project, title and who its assigned to
    parser_add_task = subparsers.add_parser("add-task", help="add a new task")
    parser_add_task.add_argument("--project", required=True, help="project title")
    parser_add_task.add_argument("--title", required=True, help="task title")
    parser_add_task.add_argument("--assigned-to", dest="assigned_to", default="unassigned", help="who is this task for")
    parser_add_task.set_defaults(func=add_task)

    # list-tasks command - no arguments needed just lists all tasks
    parser_list_tasks = subparsers.add_parser("list-tasks", help="list all tasks")
    parser_list_tasks.set_defaults(func=list_tasks)

    # complete-task command - needs the title of the task to complete
    parser_complete_task = subparsers.add_parser("complete-task", help="mark task as complete")
    parser_complete_task.add_argument("--title", required=True, help="task title")
    parser_complete_task.set_defaults(func=complete_task)

    # parse and run the command
    # if a command was given run it, otherwise show the help message
    #remember to use hasattr and parser and print
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()