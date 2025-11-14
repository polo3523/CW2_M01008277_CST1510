from apl import register_user, login_user

def menu():
    while True:
        choice = input('Choose an option: (1) Register (2) Login (3) Exit: ')
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')