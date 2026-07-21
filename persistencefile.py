# this file helps me save and load data from my json file
# i use json and os modules which are built into python
# this is where ill use the read commands
#insted of file.read and file.write ill use json.dump and json.load since its  similar thing
#remember to user "r" or not necessarily that letter but as long as does same function

import json

DATA_FILE = "data.json"

def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

#notes: i use json.load instead of file.read because json.load reads the file 
# and turns it into a python dictionary automatically so i can do thatg data["users"]
# i use json.dump instead of file.write because it saves the dictionary back to the file
# file.write only works with plain text not dictionaries. keyyyy partttt.
#hopefully it works