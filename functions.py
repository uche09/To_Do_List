import csv
from pathlib import Path
from classes import List
import datetime
import os
import plyer


def account_creation(first_name, other_name, last_name, gender, username, password):

    with open("database/users/users.csv", 'a', newline='') as users_file:
        field_names = ['first_name', 'other_name', 'last_name', 'gender', 'username', 'password']

        csv_writer = csv.DictWriter(users_file, fieldnames=field_names, delimiter=',')

        if users_file.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerow({"first_name": first_name,
                             "other_name": other_name,
                             "last_name": last_name,
                             "gender": gender,
                             "username": username,
                             "password": password})

    return print("\nYour account has been created!")


def create_user_space(username):
    path = Path(f'database/work_space/{username}')
    path.mkdir()

    list_categories = ['work', 'school', 'personal']
    for dir in list_categories:
        new_dir = path/dir
        new_dir.mkdir(exist_ok=True)
        todo_list = new_dir/f'{dir}_list.csv'
        todo_list.touch()

        with open(todo_list, 'w', newline='') as ls:
            field_names = ['title', 'description', 'due_date', 'category', 'status']

            csv_writer = csv.DictWriter(ls, fieldnames=field_names, delimiter=',')

            if ls.tell() == 0:
                csv_writer.writeheader()


def acc_logger(username, password):
    with open('database/users/users.csv', 'r') as users_file:
        users = csv.DictReader(users_file)

        for user in users:
            if user['username'] == username:
                if user['password'] == password:
                    print('login successful!')
                    return True
                else:
                    return False
            else:
                return None


def status_update(username):
    user_list = List(username)

    for cat in user_list.path.iterdir():

        for file in cat.iterdir():
            with open(f'{file}', 'r+') as all_list:
                list_reader = csv.DictReader(all_list)

                data = list(list_reader)

                fieldnames = ['title', 'description', 'due_date', 'category', 'status']
                new_data = []

                for line in data:

                    user_list_date = datetime.datetime.strptime(line["due_date"], '%Y-%m-%d %H:%M:%S')

                    if user_list_date <= datetime.datetime.now():
                        line['status'] = 'due'

                    else:
                        line['status'] = 'pending'

                    new_data.append(line)

            os.remove(f'{file}')

            with open(f"{file}", 'w', newline='') as cat_file:
                csv_writer = csv.DictWriter(cat_file, fieldnames=fieldnames)

                if cat_file.tell() == 0:
                    csv_writer.writeheader()

                csv_writer.writerows(new_data)
                new_data.clear()


def notify(title, message):
    plyer.notification.notify(
        title=title,
        message=message,
        timeout=5
    )
