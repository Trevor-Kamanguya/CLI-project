#this is the class like a child of the project, like this is the one that shows the tasks
#i can also add like a pending thing like status then when a task is done i changes to completed
#ill use self for that

class Task:
    def __init__(self, title, assigned_to):
        self.title = title
        self.assigned_to = assigned_to
        self.status = "waiting for the task to be done"

    def complete(self):
        self.status = "the task is done"

    def __str__(self):
        return f"the task: {self.title} which was assigned to this student:{self.assigned_to} is in this status: {self.status}"