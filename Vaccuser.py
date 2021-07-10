import csv
from csv import writer
from pathlib import Path
import pandas as pd
import credentials
import helper
from Vaccine import VacInfo

class Vacuser(VacInfo):

    def view_certificate(self, uid, vaccine_id=None):
        df1 = pd.read_csv('data.csv')
        df1.set_index('UID')
        for i, row in df1.iterrows():
            if i == int(uid) - 1:
                helper.generate_qr_code(row)
                print("EU Digital COVID Certificate of user", uid)
                print(row)
                a = df1.iloc[i, 8]
                b = VacInfo(vaccine_id)
                b.user_view(a)


class Admin:

    def __init__(self, vname="", fname="", gender="", DOB="", nationality="", identification="", vaccine_date="",
                 vaccine_code=""):

        self.name = vname
        self.surname = fname
        self.Gender = gender
        self.DOB = DOB
        self.nationality = nationality
        self.identification = identification
        self.vaccine_date = vaccine_date
        self.vaccine_code = vaccine_code

    def add_user(self):

        inlist = []  # list to store data
        df = pd.read_csv('data.csv')  # UID generator
        uid = len(df) + 1
        credentials.add_credentials(uid, self.identification)  # login data dictionary
        inlist.append(uid)
        inlist.append(self.name)
        inlist.append(self.surname)
        inlist.append(self.Gender)
        inlist.append(self.DOB)
        inlist.append(self.nationality)
        inlist.append(self.identification)
        inlist.append(self.vaccine_date)
        inlist.append(self.vaccine_code)
        print("....New user successfully added....")
        print("New user detailes are: ", inlist)
        if Path('data.csv').is_file():  # check if the data file is created
            with open('data.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(inlist)
                f_object.closed

        else:
            with open('data.csv', 'w') as new_file:
                csv_w = csv.writer(new_file)
                csv_w.writerow(inlist)
                new_file.closed

    def view_user(self):
        df = pd.read_csv('data.csv', error_bad_lines=False)
        print(df)
