#ill implement everything ive learnt this module for this project.
#i make sure to use git branches and commits
#objectives: You will build a Python-based Command-Line Interface (CLI) application that manages a simulated multi-user project tracker system. The CLI should allow users to:

#Create and manage users, projects, and tasks.
#Display and search projects assigned to specific users.
#Use file IO to persist data locally.
#Use pip to manage external packages (e.g., for pretty printing, date formatting, or input validation).
#Structure code using modules, classes, and object relationships.
#Document, test, and debug your solution.

#i use input incase i need to add user input. for selecing tasks
#i also use if, elif else statemenst and while loops if necessary and continue and break commands and for loops wjth like ... incase needed and then for in
#i use operators and also the int for integer
#i can also use tuples and lists and dictionaries and maybe append and like that and strings. check on canvas password lab incase i get an issue
#i implement file handling also for update lists and removing and etc. i can use file handling practise lab in canvas incase i get an issue or refernce
#i create an __init__.py file for  to mark it as a package and you import the necessary functions and variables from the module
#i import correctly and specifying
#i also use regex and tyr and raise for errors handling like for bringing errors like in input validation.
#i aslo implement algorithims if needed such as this from canvas:
# number = int(user_input)
 #   result = calculate_factorial(number)
  #  if result is not None:
   #     print("The factorial of", number, "is:", result)
#except ValueError:
 #   print("Error: Invalid input. Please enter a valid integer.")
#and also dictionary sets
#and also oop both part 1 2 and 3 utilising inheritance and super and i can use this as example just incasse i get lost: 
# 
# import random
#class User:
 #   all_names = []

  #  def __init__(self, first_name, last_name, email):
   #     self.first_name = first_name
    #    self.last_name = last_name
     #   self.email = email
      #  User.add_name_to_all(first_name, last_name)

    #def send_email(self,receiver,message):
     #   print(f"{self.email} to {receiver}: {message}") 

    #@classmethod
    #def add_name_to_all(cls,first,last):
     #   fullname = first + " " + last
      #  cls.all_names.append(fullname)

    #@classmethod
    #def user_exists(cls,fullname):
     #   return fullname in cls.all_names


#class Teacher(User):
 #   def __init__(self, first_name, last_name, email):
  #      super().__init__(first_name, last_name,email)
   #     self.knowledge = [
    #        "str is a data type in Python",
     #       "programming is hard, but it's worth it",
      #      "JavaScript async web request",
       #     "Python function call definition",
        #    "object-oriented teacher instance",
         #   "programming computers hacking learning terminal",
          #  "pipenv install pipenv shell",
           # "pytest -x flag to fail fast",
        #]

    #def teach(self):
     #   return self.knowledge[random.randint(0, len(self.knowledge) - 1)]

#class Student(User):
 #   def __init__(self, first_name, last_name, email,gpa):
  #      super().__init__(first_name, last_name,email)
   #     self.gpa = gpa
    #    self.knowledge = []
#
 #   def learn(self,knowledge_string):
  #      self.knowledge.append(knowledge_string)


#i als use relationships many to many and one to many. here specifiaclly and other parts i feel needed.
#many-to-many: User -> Projects
#One-to-many: Project -> Tasks
#i also implement File I/O (Input/Output) enables programs to interact with external files, reading and writing data for storage, logging, and data processing. really needed

#For external libraries, install them via Pip: eg
#pip install requests
#then: Then, import them in Python: 
#import requests
#response = requests.get("https://api.github.com")
#print(response.status_code)

#for reading a txt file: with open("example.txt", "r") as file:
    #content = file.read()
    #print(content)  # Outputs the file content
#for writing i just change the read to write

#i implement  PyPi, Pip & Python Scripting? 
#this is how: pip install requests
#After installation, you can import and use the package in your script:

#import requests

#response = requests.get("https://api.github.com")
#print(response.status_code)
#Uses pip to add functionality without writing everything from scratch.
#For larger projects, it’s common to list all needed packages in a requirements.txt file:
#requests
#flask
#Install all dependencies with:
#pip install -r requirements.txt
#Keeps your environment reproducible and your setup process consistent.

#for executable script, please remember: if __name__ == "__main__":
    # your code

#i use argparse for cli, example from canvas: import argparse
#parser = argparse.ArgumentParser(description="Grocery List CLI")
#parser.add_argument("item", help="Name of the grocery item")
#args = parser.parse_args()
#print(f"🛒 Added item: {args.item}")


#reference of adding tasks form canvas and listing: import argparse
"""
import argparse
def add_task(args):
    print(f" Task added: {args.description}")
def list_tasks(args):
    print(" Listing all tasks...")
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")
    add_parser.set_defaults(func=add_task)
    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.set_defaults(func=list_tasks)
    args = parser.parse_args()
    # Handle missing command
    if hasattr(args, "func"):
       args.func(args)
    else:
       parser.print_help()
in task_cli.py:
from lib.cli_tool import main
if __name__ == "__main__":
    main()"""
#then i implement using like mapping cli commands to like object methods- very familiar.like this: from canvas cli method page
"""import argparse

users = {}

def add_task(args):
    user = users.get(args.user) or User(args.user)
    users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

parser = argparse.ArgumentParser(description="User Task Manager CLI")
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser("add-task", help="Add a task to a user")
add_parser.add_argument("user", help="User's name")
add_parser.add_argument("title", help="Title of the task")
add_parser.set_defaults(func=add_task)

args = parser.parse_args()
args.func(args)
"""
#then i run it with, $ python task_cli.py add-task Alice "Write project proposal"
# Task 'Write project proposal' added to Alice's list.

#then i can implement the complete task for like showing tasks done
"""import argparse

users = {}

def add_task(args):
    user = users.get(args.user) or User(args.user)
    users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    user = users.get(args.user)
    if user:
        for task in user.tasks:
            if task.title == args.title:
                task.complete()
                return
        print("Task not found.")
    else:
        print(" User not found.")

parser = argparse.ArgumentParser(description="User Task Manager CLI")
subparsers = parser.add_subparsers()

# Add Task
add_parser = subparsers.add_parser("add-task", help="Add a task to a user")
add_parser.add_argument("user")
add_parser.add_argument("title")
add_parser.set_defaults(func=add_task)

# Complete Task
complete_parser = subparsers.add_parser("complete-task", help="Mark a task complete")
complete_parser.add_argument("user")
complete_parser.add_argument("title")
complete_parser.set_defaults(func=complete_task)

args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()"""

#i make sure to refer here as ill use as a checklist and deadline sunday midnight.
#not familiar with testing so i might skip that or refer way later after done with this.