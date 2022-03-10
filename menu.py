import bookclubQueries


def run(cursor):
    return main_menu(cursor)


def main_menu(cursor):
    print_menu()
    user_input = get_user_input("\nEnter your choice")

    if should_quit(user_input):
        return False
    elif user_input == "1":
        all_books(cursor)
    elif user_input == "2":
        all_books_from_author(cursor)
    elif user_input == "3":
        print("\nAverage rating for writer")
        wait_for_enter()
    elif user_input == "4":
        print("\nAverage rating for book")
        wait_for_enter()
    elif user_input == "5":
        print("\nMost popular book in city")
        wait_for_enter()
    elif user_input == "6":
        print("\nMember who made most reviews")
        wait_for_enter()
    elif user_input == "7":
        print("\nSee all books you have reviewed")
        wait_for_enter()

    return True


def print_menu():
    print("\n[1] List all books")
    print("[2] List all books from specific author")
    print("[3] Average rating for book")
    print("[4] Average rating for writer")
    print("[5] Most popular book in city")
    print("[6] Member who made most reviews")
    print("[7] See all books you have reviewed")
    print("\n[Q] Quit")


def should_quit(value):
    return value == "q" or value == "Q"


def all_books(cursor):
    print("\n")
    bookclubQueries.list_books(cursor)
    wait_for_enter()


def all_books_from_author(cursor):
    author = get_user_input("\nName of author")
    print("\n")
    bookclubQueries.list_books_from_author(cursor, author)
    wait_for_enter()


def get_user_input(question):
    return input(question + ": ")


def wait_for_enter():
    input("\nPress Enter to continue...")
