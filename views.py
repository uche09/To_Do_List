import csv
import functions
from pathlib import Path
from classes import List
import datetime
import os


def password_creation():
    username = input(f"*please choose a username "
                     f"(username should not contain white spaces or special characters): ")

    password = input("*choose a password (password must not be less than 8 characters): ")

    for char in username:
        if char == " ":
            print('username should not contain white spaces')
            password_creation()

        if len(password) < 8:
            print("password must not be less than 8 characters")
            password_creation()
    try:
        with open('database/users/users.csv', 'r') as user_file:
            users = csv.DictReader(user_file)
    except FileNotFoundError:
        path = Path('database/users')
        path.mkdir(parents=True)
        path = Path(f'{path}/users.csv')
        path.touch()

        with open("database/users/users.csv", 'a', newline='') as users_file:
            field_names = ['first_name', 'other_name', 'last_name', 'gender', 'username', 'password']

            csv_writer = csv.DictWriter(users_file, fieldnames=field_names, delimiter=',')

            if users_file.tell() == 0:
                csv_writer.writeheader()

        with open('database/users/users.csv', 'r') as user_file:
            users = csv.DictReader(user_file)

            for user in users:
                if user['username'] == username:
                    print('This username has already been taken!!  Try something else')
                    password_creation()

    return username, password


def registration():
    first_name = input("*Enter your first name: ")
    other_name = input("Enter other name(s): ")
    last_name = input("*Enter your last name: ")
    gender = input("*Gender (M/F/N): ")

    username, password = password_creation()
    functions.account_creation(first_name, other_name, last_name, gender,
                               username,
                               password)

    functions.create_user_space(username)
    print(f'You are logged in to {username}.\n\n')
    home(username)


def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    is_logged_in = functions.acc_logger(username, password)

    if is_logged_in is None:
        print('This account does not exist')
    elif is_logged_in:
        print('logged in successful!')
        print(f'You are logged in to {username}.\n\n')
        home(username)
    else:
        print('Your password is incorrect!')


def home(username):
    try:
        functions.status_update(username)
    except FileNotFoundError:
        pass

    print(f'''1.  {notification(username)} Notifications\n
2.  My to-do list\n
3.  Add new task to list\n
4.  Delete a task.\n
5.  Update task\n
6.  Profile\n
*.  Exit
''')
    user_option = input('>>> ')

    if user_option == '1':
        print_notification(username)
        home(username)
    elif user_option == '2':
        my_to_do_list(username)
        home(username)
    elif user_option == '3':
        add_new_task(username)
        home(username)
    elif user_option == '4':
        delete_task(username)
        home(username)
    elif user_option == '5':
        update_task(username)
        home(username)
    elif user_option == '6':
        pass
    elif user_option == '*':
        return
    else:
        print("You entered an invalid option. Please try again\n")
        home(username)


def my_to_do_list(username):
    all_list = List(username)
    print(f'''1.  See list in all category\n
2.  See lists in personal category\n
3.  See lists in school category\n
4.  See lists in work category\n
''')
    user_choice = input('>>> ')

    if user_choice == '1':
        print(all_list.all_cat())

    elif user_choice == '2':
        print(all_list.single_cat("personal"))
    elif user_choice == '3':
        print(all_list.single_cat('school'))
    elif user_choice == '4':
        print(all_list.single_cat('work'))
    else:
        print('You entered an invalid option. Try again')
        my_to_do_list(username)


def add_new_task(username):
    add_task = List(username)
    print(f'''Please select the task category:\n
1.  Add task to personal category\n
2.  Add task to school category\n
3.  Add task to work category\n
''')
    user_choice = input('>>> ')

    if user_choice == '1':
        add_task.add_to_list('personal')

    elif user_choice == '2':
        add_task.add_to_list('school')

    elif user_choice == '3':
        add_task.add_to_list('work')

    else:
        print('You entered an invalid option. Please try again\n')
        add_new_task(username)


def update_task(username):
    task_list = List(username)

    print(f'''\n\nPlease select a task category:\n
    1.  Update task in personal category\n
    2.  Update task in school category\n
    3.  Update task in work category\n
    4:  Go back''')
    user_choice = input('>>> ')

    if user_choice == '1':
        category = 'personal'
        print(task_list.single_cat(category))
        line_index = int(input('Enter the task number you want to update: '))

        print('\n1:  Update entire detail of task\n'
              '2:  Update specific field in task')
        option = input('>>> ')
        if option == '1':

            task_list.update_list_row(category, line_index)
            print('\nDo you wish to edit another task?\n'
                  '1: Yes\n'
                  '2: No')
            option2 = input('>>> ')

            if option2 == '1':
                update_task(username)
            elif option2 == '2':
                home(username)
            else:
                print('You entered an invalid option')
                home(username)

        elif option == '2':

            task_list.update_list_field(category, line_index)
            print('\nDo you wish to edit another task?\n'
                  '1: Yes\n'
                  '2: No')
            option2 = input('>>> ')

            if option2 == '1':
                update_task(username)
            elif option2 == '2':
                home(username)
            else:
                print('You entered an invalid option')
                home(username)
        else:
            print('You entered an invalid option')
            update_task(username)

    elif user_choice == '2':
        category = 'school'
        print(task_list.single_cat(category))
        line_index = int(input('Enter the task number you want to update: '))

        print('\n1:  Update entire detail of task\n'
              '2:  Update specific field in task')
        option = input('>>> ')
        if option == '1':

            task_list.update_list_row(category, line_index)
            print('\nDo you wish to edit another task?\n'
                  '1: Yes\n'
                  '2: No')
            option2 = input('>>> ')

            if option2 == '1':
                update_task(username)
            elif option2 == '2':
                home(username)
            else:
                print('You entered an invalid option')
                home(username)

        elif option == '2':

            task_list.update_list_field(category, line_index)
            print('\nDo you wish to edit another task?\n'
                  '1: Yes\n'
                  '2: No')
            option2 = input('>>> ')

            if option2 == '1':
                update_task(username)
            elif option2 == '2':
                home(username)
            else:
                print('You entered an invalid option')
                home(username)
        else:
            print('You entered an invalid option')
            update_task(username)

    elif user_choice == '3':
        category = 'work'
        print(task_list.single_cat(category))
        line_index = int(input('Enter the task number you want to update: '))

        print('\n1:  Update entire detail of task\n'
              '2:  Update specific field in task')
        option = input('>>> ')

        if option == '1':

            task_list.update_list_row(category, line_index)
            print('\nDo you wish to edit another task?\n'
                  '1: Yes\n'
                  '2: No')
            option2 = input('>>> ')

            if option2 == '1':
                update_task(username)
            elif option2 == '2':
                home(username)
            else:
                print('You entered an invalid option')
                home(username)

        elif option == '2':

            task_list.update_list_field(category, line_index)
            print('\nDo you wish to edit another task?\n'
                  '1: Yes\n'
                  '2: No')
            option2 = input('>>> ')

            if option2 == '1':
                update_task(username)
            elif option2 == '2':
                home(username)
            else:
                print('You entered an invalid option')
                home(username)
        else:
            print('You entered an invalid option')
            update_task(username)

    elif user_choice == '4':
        home(username)
    else:
        print('You entered an invalid option2')
        update_task(username)


def delete_task(username):
    task_list = List(username)

    print(f'''\n\nPlease select a task category:\n
1.  Delete task in personal category\n
2.  Delete task in school category\n
3.  Delete task in work category\n
4:  Go back''')
    user_choice = input('>>> ')

    if user_choice == '1':
        category = 'personal'
        print(task_list.single_cat(category))
        line_index = int(input('Enter the task number you want to delete: '))

        task_list.del_task(category, line_index)

    elif user_choice == '2':
        category = 'school'
        print(task_list.single_cat(category))
        line_index = int(input('Enter the task number you want to delete: '))

        task_list.del_task(category, line_index)

    elif user_choice == '3':
        category = 'work'
        print(task_list.single_cat(category))
        line_index = int(input('Enter the task number you want to delete: '))

        task_list.del_task(category, line_index)

    elif user_choice == '4':
        home(username)
    else:
        print('You entered an invalid option2')
        delete_task(username)


def notification(username):
    TITLE = 'Pending Task!'
    path = Path(f'database/notifications')
    notification_list = Path(f'{path}/{username}.txt')

    _5days = datetime.timedelta(days=4)

    user_list = List(username)

    try:
        os.remove(f'{path}/{username}.txt')
    except FileNotFoundError:
        path.mkdir(parents=True)
        notification_list.touch()

    for cat in user_list.path.iterdir():

        for file in cat.iterdir():
            with open(f'{file}', 'r+') as all_list:
                list_reader = csv.DictReader(all_list)

                data = list(list_reader)
                notification_list.touch()

                with open(f"{path}/{username}.txt", 'a', newline='') as note_file:
                    for line in data:

                        user_list_date = datetime.datetime.strptime(line["due_date"], '%Y-%m-%d %H:%M:%S')

                        if user_list_date > datetime.datetime.now():
                            days_to_due = user_list_date - datetime.datetime.now()

                            if days_to_due <= _5days:
                                message = f"You have {days_to_due.days} day(s) left to finish {line['title']}\n"
                                functions.notify(TITLE, message)
                                note_file.write(message)

                            else:
                                pass

    with open(f'{path}/{username}.txt', 'r', newline='') as note:
        lines = note.readlines()
        length = len(lines)
    return length


def print_notification(username):
    path = Path(f'database/notifications/{username}.txt')

    with open(f"{path}", 'r', newline='') as note:
        lines = note.readlines()
        for line in lines:
            print(line)
