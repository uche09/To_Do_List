import views
# import functions

user_option = ''

while user_option != "*":
    print(f'''\n Welcome to UC console To-do list manager
    Please enter the numbers associated with the option of your choice.\n
    
    1: Create an account
    2: Login if you already have an account
    *: Exit''')
    user_option = input('>>> ')

    if user_option == '1':
        views.registration()
    elif user_option == '2':
        views.login()
    else:
        continue
