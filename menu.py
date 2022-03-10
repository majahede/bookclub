def run():
    return main_menu()


def main_menu():
    print_menu()
    user_input = get_user_input("\nEnter your choice")

    if should_quit(user_input):
        return False
    elif user_input == "1":
        print("\nAverage rating for book")
        wait_for_enter()
    elif user_input == "2":
        print("\nAverage rating for writer")
        wait_for_enter()
    elif user_input == "3":
        print("\nMost popular book in city")
        wait_for_enter()
    elif user_input == "4":
        print("\nMember who made most reviews")
        wait_for_enter()
    elif user_input == "5":
        print("\nSee all books you have reviewed")
        wait_for_enter()

    return True


def print_menu():
    print("\n[1] Average rating for book")
    print("[2] Average rating for writer")
    print("[3] Most popular book in city")
    print("[4] Member who made most reviews")
    print("[5] See all books you have reviewed")
    print("\n[Q] Quit")


def should_quit(value):
    return value == "q" or value == "Q"


def get_user_input(question):
    return input(question + ": ")


def wait_for_enter():
    input("\nPress Enter to continue...")
