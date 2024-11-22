import currency_api
import history_manager

def show_menu():
    print("1. Convert currency")
    print("2. View conversion history")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        currency_api.convert_currency()
    elif choice == '2':
        history_manager.view_history()
    elif choice == '3':
        exit()
    else:
        print("Invalid choice. Try again.")
