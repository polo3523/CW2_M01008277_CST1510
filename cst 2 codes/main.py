from application import register_user, login_user


def menu():
    print("*" * 30)
    print("Welcome to the User System (Terminal)")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("*" * 30)


def main():
    while True:
        menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter new username: ")
            pw = input("Enter new password: ")
            success, message = register_user(name, pw)  # Pass inputs to SQL function
            print(message)

        elif choice == '2':
            name = input("Enter username: ")
            pw = input("Enter password: ")
            success, message = login_user(name, pw)  # Pass inputs to SQL function
            print(message)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()