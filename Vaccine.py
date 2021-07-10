import csv
from csv import writer
from pathlib import Path

import pandas as pd


# This is the "Capital" Vaccine super class and defined "small" vaccine as a method

class VacInfo:
    def __init__(self, vaccine_name="", vaccine_id="", number_of_doses="", origin=""):

        self.vaccine_name = vaccine_name
        self.vaccine_id = vaccine_id
        self.number_of_doses = number_of_doses
        self.origin = origin

    def viewvac(self):
        with open('vaccine.csv', 'r') as vf:
            csv_reader = csv.reader(vf)
            for line in csv_reader:
                print(line)

    def add_info(self):
        inlist = []
        inlist.append(self.vaccine_name)
        inlist.append(self.vaccine_id)
        inlist.append(self.number_of_doses)
        inlist.append(self.origin)

        print("....New vaccine's information successfully added....")
        print("New vaccine details are: ", inlist)
        if Path('vaccine.csv').is_file():
            with open('vaccine.csv', 'a') as vf:
                writer_object = writer(vf)
                writer_object.writerow(inlist)
                vf.closed

        else:
            with open('vaccine.csv', 'w') as nf:
                csv_w = csv.writer(nf)
                csv_w.writerow(inlist)

    def user_view(self, vaccine_ID):
        df2 = pd.read_csv('vaccine.csv')
        df2.set_index('Vaccine_ID')
        for i, row in df2.iterrows():
            if i == vaccine_ID - 1:
                print(row)
