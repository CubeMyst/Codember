import requests
import re

def is_valid(entry):
    id, username, email, age, location = entry
    if not re.match("^[a-zA-Z0-9]*$", id):
        return False
    if not re.match("^[a-zA-Z0-9]*$", username):
        return False
    if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False
    if age and not age.isdigit():
        return False
    return True

response = requests.get('https://codember.dev/data/database_attacked.txt')
lines = response.text.split('\n')
message = ''

for line in lines:
    entry = line.split(',')
    if not is_valid(entry):
        message += entry[1][0]

print(f'submit {message}')
