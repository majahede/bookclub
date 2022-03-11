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
        average_rating_for_book(cursor)
    elif user_input == "4":
        average_rating_for_writer(cursor)
    elif user_input == "5":
        most_popular_book(cursor)
    elif user_input == "6":
        all_members_ordered_by_review(cursor)
    elif user_input == "7":
        all_members_books(cursor)
    elif user_input == "8":
        all_books_from_author_view(cursor)

    return True


def print_menu():
    print("\n[1] List all books")
    print("[2] List all books from specific author")
    print("[3] Average rating for book")
    print("[4] Average rating for writer")
    print("[5] Most popular book in city")
    print("[6] List all members by books reviewed")
    print("[7] See all books you have reviewed")
    print("[8] List books from author (view)")
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


def average_rating_for_book(cursor):
    book = get_user_input("\nBook title")
    bookclubQueries.average_rating_book(cursor, book)
    wait_for_enter()


def average_rating_for_writer(cursor):
    author = get_user_input("\nAuthor name")
    bookclubQueries.average_rating_writer(cursor, author)
    wait_for_enter()


def most_popular_book(cursor):
    city = get_user_input("\nName of city")
    print("\n")
    bookclubQueries.most_popular_book(cursor, city)
    wait_for_enter()

def all_members_ordered_by_review(cursor):
    print("\n")
    bookclubQueries.list_member_by_reviews(cursor)
    wait_for_enter()


def all_books_from_author_view(cursor):
    author = get_user_input("\nName of author")
    print("\n")
    bookclubQueries.author_view(cursor, author)
    wait_for_enter()


def all_members_books(cursor):
    member = get_user_input("\nEnter member name")
    print("\n")
    bookclubQueries.list_members_books(cursor, member)
    wait_for_enter()


def get_user_input(question):
    return input(question + ": ")


def wait_for_enter():
    input("\nPress Enter to continue...")
