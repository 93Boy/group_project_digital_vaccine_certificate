import hashlib
import json
import os


def login():
    if not os.path.isfile("credentials.json"):
        raise FileNotFoundError("Credentials file not found.")
    with open("credentials.json", "r") as credentials_file:
        credentials = json.load(credentials_file)

    login_attempt = 0

    while True:
        login_attempt += 1
        if login_attempt > 3:
            print("You have exceeded number of attempts.")
            return None

        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        if credentials.get(username) == hashlib.sha224(bytes(password, 'utf-8')).hexdigest():
            print("Successful login.")
            return username
        else:
            print("Incorrect credentials.")


def add_credentials(username, password):
    if not os.path.isfile("credentials.json"):
        with open('credentials.json', 'w') as credentials_file:
            credentials_file.write("{}")

    with open('credentials.json', 'r+') as credentials_file:
        credentials = json.load(credentials_file)
        credentials[username] = hashlib.sha224(bytes(password, 'utf-8')).hexdigest()
        credentials_file.seek(0)
        json.dump(credentials, credentials_file, indent=4)
