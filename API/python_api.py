import requests
import json
import sys

parameter = sys.argv[1]
user_url = f"https://jsonplaceholder.typicode.com/users/{parameter}"
task_url = f"https://jsonplaceholder.typicode.com/todos/"

# calling a requests.get request t0 tasks and users which will respond witht the item with id 1
user_response = requests.get(user_url)
task_response = requests.get(task_url)

# call json on the response object to view the data that is sent back by the API
user_resp = user_response.json()
task_resp = task_response.json()

# counting the tasks of userid given in the command_line
tasks = 0
completed_tasks = 0

# looping a list of dictionaries
for my_dicts in task_resp:
    if my_dicts.get("userId") == int(parameter):
        tasks += 1
        if my_dicts.get("completed") == True:
            completed_tasks += 1
        #print()
        #print(my_dicts)

name = user_resp["name"]
print(f"Employee {name} is done with tasks({completed_tasks}/{tasks}):")

# looping a list of and printing only the tasks done
for my_dicts in task_resp:
    if my_dicts.get("userId") == int(parameter) and my_dicts.get("completed") == True:
        print("\t ",my_dicts.get("title"))

