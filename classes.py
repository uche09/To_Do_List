import csv
from pathlib import Path
import datetime
from collections import OrderedDict


class List:
    def __init__(self, username):
        self.username = username

        self.path = Path(f'database/{self.username}')

    def all_cat(self):
        for cat in self.path.iterdir():

            for file in cat.iterdir():
                with open(f'{file}', 'r') as all_list:
                    list_reader = csv.DictReader(all_list)

                    for line in list_reader:
                        self.date = datetime.datetime.strptime(f'{line["due_date"]}', '%Y-%m-%d %H:%M:%S')

                        return f'{line["title"]}, {line["description"]}, ' \
                               f'{self.date.strftime("%d %b, %Y %I:%M %p")}, {line["status"]}'

    def single_cat(self, category):

        with open(f'{self.path}/{category}/{category}_list.csv', 'r') as single_list:
            list_reader = csv.DictReader(single_list)

            for line in list_reader:
                self.date = datetime.datetime.strptime(f'{line["due_date"]}', '%Y-%m-%d %H:%M:%S')

                return f'{line["title"]}, {line["description"]}, ' \
                       f'{self.date.strftime("%d %b, %Y %I:%M %p")}, {line["status"]}'

    def add_to_list(self, category):
        self.title = input('Enter task name: ')
        self.description = input('Describe task (in few words): ')
        self.year = input("Enter year of due date in full (2017): ")
        self.month = input("Enter month of due date in short (Aug): ")
        self.day = input("Enter day of due date (09): ")

        self.hour = input("Enter the hour of due time (using 12 hours timing): ")
        self.minute = input("Enter the minute of due time: ")
        self.meridia = input("AM or PM?: ")
        self.status = ''

        try:
            self.due_date = datetime.datetime.strptime(f"{self.day} {self.month}, {self.year}    "
                                                       f"{self.hour}:{self.minute} {self.meridia}",
                                                       '%d %b, %Y    %I:%M %p')
        except ValueError:
            print('\nYou entered the wrong date/time format. Please try again\n\n')
            self.add_to_list(category)

        fieldnames = ['title', 'description', 'due_date', 'status']

        with open(f"database/{self.username}/{category}/{category}_list.csv", 'a', newline='') as cat_file:
            csv_writer = csv.DictWriter(cat_file, fieldnames=fieldnames)

            if cat_file.tell() == 0:
                csv_writer.writeheader()

            if self.due_date > datetime.datetime.now():
                self.status = 'pending'
            else:
                self.status = 'due'

            csv_writer.writerow({'title': self.title, 'description': self.description,
                                 'due_date': self.due_date, 'status': self.status})

        print('\nnew task added!')
