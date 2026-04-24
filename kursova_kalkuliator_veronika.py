import math
from datetime import datetime, timedelta

from db_manager import get_all_users, save_all_users, get_all_history, save_history_record


def register_new_user():
    print("\n--- REGISTRATION ---")
    all_users_list = get_all_users()

    registration_login = input("Enter new login: ").strip()
    registration_password = input("Enter new password: ").strip()
    registration_password_repeat = input("Repeat your password: ").strip()

    if registration_login == "" or registration_password == "":
        print("Error: Login or password cannot be empty!")
        return

    if registration_password != registration_password_repeat:
        print("Error: Passwords do not match!")
        return

    for existing_user in all_users_list:
        if existing_user['login'] == registration_login:
            print("Error: This login is already taken!")
            return

    if len(all_users_list) == 0:
        new_user_id = 1
    else:
        new_user_id = all_users_list[-1]['id'] + 1

    new_user_object = {
        "id": new_user_id,
        "login": registration_login,
        "password": registration_password
    }

    all_users_list.append(new_user_object)
    save_all_users(all_users_list)
    print("Registration successful! You can now login.")


def login_user():
    print("\n--- LOGIN ---")
    all_users_list = get_all_users()
    login_attempts_count = 3

    while login_attempts_count > 0:
        login_attempt_name = input("Enter login: ").strip()
        password_attempt_string = input("Enter password: ").strip()

        for user_item in all_users_list:
            if user_item['login'] == login_attempt_name and user_item['password'] == password_attempt_string:
                print("Welcome, " + user_item['login'] + "! You have successfully logged in.")
                return user_item

        login_attempts_count -= 1
        if login_attempts_count > 0:
            print(f"Incorrect login or password. Attempts remaining: {login_attempts_count}")
        else:
            print("Attempts exhausted. Access blocked.")

    return None

def run_calculator(current_user):
    print("\n--- CALCULATOR STARTED ---")
    operations_count = 0

    if current_user == None:
        user_status = "guest"
        current_user_id = 0
    else:
        user_status = "user"
        current_user_id = current_user['id']

    while True:
        if user_status == "guest" and operations_count >= 5:
            print("Limit for guest mode (5 operations) reached. Please register!")
            break

        print("\nAvailable actions: +, -, *, /, sin, cos, tan, ctg, history, exit")
        user_command = input("Choose action: ").strip().lower()

        if user_command == 'exit':
            break

        if user_command == 'history':
            if user_status == "guest":
                print("History is not available for guests. Please login.")
                continue

            history_data = get_all_history()
            time_limit_24_hours = datetime.now() - timedelta(hours=24)

            print(f"\n--- History for {current_user['login']} (Last 24h) ---")
            found_records = False
            for record in history_data:
                if record['user_id'] == current_user_id:
                    record_date = datetime.strptime(record['date'], "%Y-%m-%d %H:%M:%S")
                    if record_date >= time_limit_24_hours:
                        print(f"[{record['date']}] {record['operation']}")
                        found_records = True

            if not found_records:
                print("No operations found for the last 24 hours.")
            continue

        try:
            first_number = float(input("Enter number: "))
            result_string = ""

            if user_command in ['+', '-', '*', '/']:
                second_number = float(input("Enter second number: "))
                if user_command == '+':
                    calculation_result = first_number + second_number
                elif user_command == '-':
                    calculation_result = first_number - second_number
                elif user_command == '*':
                    calculation_result = first_number * second_number
                elif user_command == '/':
                    if second_number == 0:
                        print("Error: Division by zero is not allowed!")
                        continue
                    calculation_result = first_number / second_number

                result_string = f"{first_number} {user_command} {second_number} = {calculation_result}"

            elif user_command in ['sin', 'cos', 'tan', 'ctg']:
                if user_status == "guest":
                    print("Trigonometric functions are only for registered users!")
                    continue

                angle_in_radians = math.radians(first_number)
                if user_command == 'sin':
                    calculation_result = math.sin(angle_in_radians)
                elif user_command == 'cos':
                    calculation_result = math.cos(angle_in_radians)
                elif user_command == 'tan':
                    calculation_result = math.tan(angle_in_radians)
                elif user_command == 'ctg':
                    calculation_result = 1 / math.tan(angle_in_radians)

                result_string = f"{user_command}({first_number}) = {calculation_result}"
            else:
                print("Invalid command. Please try again.")
                continue

            print("Result:", calculation_result)
            operations_count += 1

            if operations_count % 3 == 0:
                print("You are actively using the calculator!")

            history_data_list = get_all_history()
            if len(history_data_list) == 0:
                new_history_id = 1
            else:
                new_history_id = history_data_list[-1]['id'] + 1

            history_record_object = {
                "id": new_history_id,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "operation": result_string,
                "user_id": current_user_id
            }

            history_data_list.append(history_record_object)
            save_history_record(history_data_list)

        except ValueError:
            print("Error: You must enter a valid number, not text!")


def main():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Guest mode")
        print("4. Exit")

        main_menu_choice = input("Your choice: ").strip()

        if main_menu_choice == '1':
            register_new_user()
        elif main_menu_choice == '2':
            logged_in_user = login_user()
            if logged_in_user != None:
                run_calculator(logged_in_user)
        elif main_menu_choice == '3':
            run_calculator(None)
        elif main_menu_choice == '4':
            print("Exiting program. Goodbye!")
            break

main()