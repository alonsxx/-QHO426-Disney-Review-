def display_title():
    print("\n=== Disneyland Review Analysis ===")


def display_main_menu():
    print("\nMain Menu:")
    print("A. View Data")
    print("B. View Charts")
    print("C. Export Data")
    print("Q. Quit")


def get_user_choice(prompt="Enter your choice: "):
    user_input = input(prompt)
    user_input = user_input.strip()  # Remove extra spaces
    user_input = user_input.upper()  # Convert to uppercase (so 'a' or 'A' both work)
    return user_input


def confirm_choice(choice):
    print("You selected:", choice)


def display_view_data_submenu():
    print("\nView Data Submenu:")
    print("1. Show all reviews for a park")
    print("2. Count reviews by location")
    print("3. Average rating by park and year")
    print("4. Back to Main Menu")
