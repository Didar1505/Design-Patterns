from admin import add_user, show_user, show_all_users

def main():
    while True:
        print("\n=== Simple DB Menu ===")
        print("1. Add user")
        print("2. Show user")
        print("3. List all users")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            role = input("Role: ")
            add_user(username, role)

        elif choice == "2":
            username = input("Username: ")
            show_user(username)

        elif choice == "3":
            show_all_users()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
