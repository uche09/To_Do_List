import csv
import os
from pathlib import Path
import datetime


class List:
    def __init__(self, username):
        self.username = username

        self.path = Path(f'database/work_space/{self.username}')

    def all_cat(self):
        for cat in self.path.iterdir():
            print('\n'+cat.name)

            for file in cat.iterdir():
                with open(f'{file}', 'r') as all_list:
                    list_reader = csv.DictReader(all_list)

                    for index, line in enumerate(list_reader):
                        self.date = datetime.datetime.strptime(f'{line["due_date"]}', '%Y-%m-%d %H:%M:%S')

                        print(f'{index + 1}: {line["title"]}, {line["description"]}, '
                              f'{self.date.strftime("%d %b, %Y %I:%M %p")}, {line["category"]}, '
                              f'{line["status"]}\n')
        return ''

    def single_cat(self, category):

        with open(f'{self.path}/{category}/{category}_list.csv', 'r') as single_list:
            list_reader = csv.DictReader(single_list)
            print('\n' + category)
            for index, line in enumerate(list_reader):
                self.date = datetime.datetime.strptime(f'{line["due_date"]}', '%Y-%m-%d %H:%M:%S')

                print(f'{index + 1}: {line["title"]}, {line["description"]}, '
                      f'{self.date.strftime("%d %b, %Y %I:%M %p")}, {line["category"]}, {line["status"]}\n')
        return ''

    def add_to_list(self, category):
        self.title = input('Enter task name: ')
        self.description = input('Describe task (in few words): ')
        self.year = input("Enter year of due date in full (2017): ")
        self.month = input("Enter month of due date in short (Aug): ")
        self.day = input("Enter day of due date (09): ")

        self.hour = input("Enter the hour of due time (using 12 hours timing): ")
        self.minute = input("Enter the minute of due time: ")
        self.meridian = input("AM or PM?: ")
        self.status = ''

        try:
            self.due_date = datetime.datetime.strptime(f"{self.day} {self.month}, {self.year}    "
                                                       f"{self.hour}:{self.minute} {self.meridian}",
                                                       '%d %b, %Y    %I:%M %p')
        except ValueError:
            print('\nYou entered the wrong date/time format. Please try again\n\n')
            self.add_to_list(category)

        fieldnames = ['title', 'description', 'due_date', 'category', 'status']

        with open(f"{self.path}/{category}/{category}_list.csv", 'a', newline='') as cat_file:
            csv_writer = csv.DictWriter(cat_file, fieldnames=fieldnames)

            if cat_file.tell() == 0:
                csv_writer.writeheader()

            if self.due_date > datetime.datetime.now():
                self.status = 'pending'
            else:
                self.status = 'due'

            csv_writer.writerow({'title': self.title, 'description': self.description,
                                 'due_date': self.due_date, 'category': category, 'status': self.status})

    def update_list_field(self, category, line_index):

        with open(f'{self.path}/{category}/{category}_list.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            lines = list(csv_reader)

        if line_index < 1 or line_index > (len(lines) + 1):
            print('This task number does not exist in task list. Please enter a valid number\n'
                  '1: Re-enter task number\n'
                  '2: Go back\n')
            option = input('>>> ')

            if option == '1':
                self.new_line_index = input('Re-enter task number: ')
                self.update_list_field(category, self.new_line_index)
            elif option == '2':
                return
            else:
                print('You entered an invalid option')
                return

        print(f'\nWhat field do you want to update?:\n'
              f'1: Title\n'
              f'2: Description\n'
              f'3: Due_date\n'
              f'4: Category\n'
              f'5: Satus')
        user_option = int(input('>>> '))

        if user_option == 3:
            self.year = input("Enter year of due date in full (2017): ")
            self.month = input("Enter month of due date in short (Aug): ")
            self.day = input("Enter day of due date (09): ")

            self.hour = input("Enter the hour of due time (using 12 hours timing): ")
            self.minute = input("Enter the minute of due time: ")
            self.meridian = input("AM or PM?: ")
            self.status = ''

            try:
                self.due_date = datetime.datetime.strptime(f"{self.day} {self.month}, {self.year}    "
                                                           f"{self.hour}:{self.minute} {self.meridian}",
                                                           '%d %b, %Y    %I:%M %p')
            except ValueError:
                print('\nYou entered the wrong date/time format. Please try again\n\n')
                self.update_list_field(category, line_index)

            lines[line_index][user_option - 1] = self.due_date

        elif user_option < 3 or user_option < 6:
            new_value = input('Enter the new value for this field: ')
            lines[line_index][user_option - 1] = new_value

        else:
            print('You entered an invalid option')
            self.update_list_field(category, line_index)

        os.remove(f'{self.path}/{category}/{category}_list.csv')
        # lines.pop(line_index-1)

        with open(f'{self.path}/{category}/{category}_list.csv', 'w', newline='') as new_file:
            csv_writer2 = csv.writer(new_file)
            csv_writer2.writerows(lines)

    def update_list_row(self, category, line_index):
        print()
        self.title = input('Enter task name: ')
        self.description = input('Describe task (in few words): ')
        self.year = input("Enter year of due date in full (2017): ")
        self.month = input("Enter month of due date in short (Aug): ")
        self.day = input("Enter day of due date (09): ")

        self.hour = input("Enter the hour of due time (using 12 hours timing): ")
        self.minute = input("Enter the minute of due time: ")
        self.meridian = input("AM or PM?: ")
        self.status = ''

        try:
            self.due_date = datetime.datetime.strptime(f"{self.day} {self.month}, {self.year}    "
                                                       f"{self.hour}:{self.minute} {self.meridian}",
                                                       '%d %b, %Y    %I:%M %p')
        except ValueError:
            print('\nYou entered the wrong date/time format. Please try again\n\n')
            self.update_list_row(category, line_index)

        with open(f'{self.path}/{category}/{category}_list.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            lines = list(csv_reader)

        if line_index < 1 or line_index > (len(lines) + 1):
            print('This task number does not exist in task list. Please enter a valid number\n'
                  '1: Re-enter task number\n'
                  '2: Go back\n')
            option = input('>>> ')

            if option == '1':
                self.new_line_index = input('Re-enter task number: ')
                self.update_list_field(category, self.new_line_index)
            elif option == '2':
                return
            else:
                print('You entered an invalid option')
                return

        if self.due_date > datetime.datetime.now():
            self.status = 'pending'
        else:
            self.status = 'due'

        lines[line_index][0] = self.title
        lines[line_index][1] = self.description
        lines[line_index][2] = self.due_date
        lines[line_index][3] = category
        lines[line_index][4] = self.status

        os.remove(f'{self.path}/{category}/{category}_list.csv')

        with open(f'{self.path}/{category}/{category}_list.csv', 'w', newline='') as new_file:
            csv_writer2 = csv.writer(new_file)
            csv_writer2.writerows(lines)

    def del_task(self, category, line_index):
        with open(f'{self.path}/{category}/{category}_list.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            lines = list(csv_reader)

        if int(line_index) < 1 or int(line_index) > (len(lines) + 1):
            print('This task number does not exist in task list. Please enter a valid number\n'
                  '1: Re-enter task number\n'
                  '2: Go back\n')
            option = input('>>> ')

            if option == '1':
                self.new_line_index = input('Re-enter task number: ')
                self.del_task(category, self.new_line_index)
            elif option == '2':
                return
            else:
                print('You entered an invalid option')
                return

        try:
            lines.pop(line_index)

            os.remove(f'{self.path}/{category}/{category}_list.csv')

            with open(f'{self.path}/{category}/{category}_list.csv', 'w', newline='') as new_file:
                csv_writer2 = csv.writer(new_file)
                csv_writer2.writerows(lines)
        except IndexError:
            print("No such task in list\n")

        print("Task has been deleted!\n")
