import csv
from classes import List
import functions


def password_creation():
    username = input(f"*please choose a username "
                     f"(username should not contain white spaces or special characters): ")

    password = input("*choose a password (password must not be less than 8 characters): ")

    for char in username:
        if char == " ":
            print('username should not contain white spaces')
            password_creation()

    with open('database/users.csv', 'r') as user_file:
        users = csv.DictReader(user_file)

        for user in users:
            if user['username'] == username:
                print('This username has already been taken!!  Try something else')
                password_creation()

    if len(password) < 8:
        print("password must not be less than 8 characters")
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


def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    login = functions.acc_logger(username, password)


def home(username):
    print(f'''You are logged in to {username}.\n\n
1.  Notifications\n
2.  My to-do list\n
3.  Add new task to list\n
4.  Delete a task.\n
5.  Update task\n
6.  Profile\n
''')


def my_to_do_list(username):
    all_list = List(username)
    print(f'''1.    See list in all category\n
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
        print('You entered an invalid option')


def add_new_task(username):
    # add_task = List(username)
    print(f'''Please select a task category:\n
1.  See lists in personal category\n
2.  See lists in school category\n
3.  See lists in work category\n
''')
    user_choice = input('>>> ')

    # if user_choice == '1':
    #     print(all_list.all_cat())
    #
    # elif user_choice == '2':
    #     print(all_list.single_cat("personal"))
    # elif user_choice == '3':
    #     print(all_list.single_cat('school'))
    # elif user_choice == '4':
    #     print(all_list.single_cat('work'))
    # else:
    #     print('You entered an invalid option')