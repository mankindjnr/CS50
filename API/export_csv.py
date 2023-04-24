import requests
import json
import sys
import csv

parameter = sys.argv[1]
user_url = f"https://jsonplaceholder.typicode.com/users/{parameter}"
task_url = f"https://jsonplaceholder.typicode.com/todos/"

# calling a requests.get request t0 tasks and users which will respond witht the item with id 1
user_response = requests.get(user_url)
task_response = requests.get(task_url)

# call json on the response object to view the data that is sent back by the API
user_resp = user_response.json()
task_resp = task_response.json()

print(type(user_resp))

print(user_resp["username"])
