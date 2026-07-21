#this is the file containing users like representing the users in the system.
#i use inheritance maybe two classes for person and user
#i also use property and name setters and track data also. less goo

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f" name is:{self.name}  and the email:({self.email})"


class User(Person):
    user_count = 0

    def __init__(self, name, email):
        super().__init__(name, email)
        self.projects = []
        User.user_count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            print("please put a name because  the name cannot be empty")
        else:
            self._name = value

    def add_project(self, project):
        self.projects.append(project)

    def __str__(self):
        return f"the User is : {self.name} and his/her emmail: {self.email} moreover, the projects for him/her: {len(self.projects)}"