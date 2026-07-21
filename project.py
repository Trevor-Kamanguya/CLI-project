#this is like for the proects that belong to a user 

class Project:
    def __init__(self, title, description, due_date, owner):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.owner = owner
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"the project name is this: {self.title} and moreover, the due date for project completion is Due: {self.due_date}. the owner of project is: {self.owner} and tasks required is: {len(self.tasks)}"
    #im using len to calculate the number of tasks in the project