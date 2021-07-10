import hashlib
import json
import json
import os
from datetime import datetime

import credentials
from Vaccine import VacInfo
from Vaccuser import Admin
from Vaccuser import Vacuser


def is_admin(user: str) -> bool:
    if not os.path.isfile("admin.json"):
        raise FileNotFoundError("Settings file not found.")
    settings_file = open("admin.json", "r")
    settings = json.load(settings_file)
    settings_file.close()

    admins = set(settings.get("admins"))
    if user in admins:
        return True
    else:
        return False


user = credentials.login()
if user is None:
    exit(1)

print(f'You are logged in as {user}.')

if is_admin(user):
    while True:
        print("Welcome to administrator interface. Please choose an option:")
        print("1 - Add new vaccine   2 - View user database  3 - Add new user   4 - Exit the program")
        choice = input("Your choice: ")
        if choice == "1":
            vaccine_Name = input("Please enter new vaccine name: ")
            vaccine_id = input("Please enter new vaccine id: ")
            Number_of_doses = input("Please enter the total number of doses: ")
            origin = input("Please enter the country of origin: ")
            a = VacInfo(vaccine_Name, vaccine_id, Number_of_doses, origin)
            a.add_info()
        elif choice == "2":
            b = Admin()
            b.view_user()
        elif choice == "3":
            vname = input("Please enter new user first name: ")
            fname = input("Please enter new user family name: ")
            Gender = input("Please enter new user gender as M:Male , F:Female , O:Other ")
            DOB = input("Please enter user Date of birth in the format of DD.MM.YYYY: ")
            format = "%d.%m.%Y"
            try:
                datetime.strptime(DOB, format)
            except ValueError:
                print("This is the incorrect date string format. It should be DD.MM.YYYY")
            Nationality = input("Please enter new user nationality: ")
            Identification = input("Please enter user social security number: ")
            Vaccination_Date = input("Please enter the vaccination date as DD.MM.YYYY: ")
            try:
                datetime.strptime(DOB, format)
            except ValueError:
                print("This is the incorrect date string format. It should be DD.MM.YYYY")
            Vaccine_Code = input("Please enter the vaccine code: ")
            b = Admin(vname, fname, Gender, DOB, Nationality, Identification, Vaccination_Date, Vaccine_Code)
            b.add_user()
        elif choice == "4":
            break
        else:
            print("Incorrect input")
else:
    d = Vacuser()
    d.view_certificate(user)
    date = datetime.now()
    print("Date of issue: ", date.strftime("%d/%m/%Y %H:%M:%S"))

"""
Hashed passwords for users
Jack - 1234 - admin
print(hashlib.sha224(b"23445").hexdigest())
"""

