import setup

USER = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'

DB_NAME = 'bookclub'
DB_BOOK_TABLE = 'books'
DB_MEMBER_TABLE = 'members'
DB_REVIEW_TABLE = 'reviews'


cnx = setup.connect_database(USER, PASSWORD, HOST, DB_NAME)
cursor = cnx.cursor()

setup.drop_table(cursor, DB_BOOK_TABLE)
setup.drop_table(cursor, DB_MEMBER_TABLE)
setup.drop_table(cursor, DB_REVIEW_TABLE)

setup.create_books_table(cursor)
setup.create_members_table(cursor)
setup.create_reviews_table(cursor)

setup.insert_books(cursor)
setup.insert_members(cursor)
setup.insert_reviews(cursor)

cnx.commit()


# list_books()
# average_rating()
# list_books_from_author()
# books_by_year()
# average_age()
# average_age_by_city()
# author_reviews()
# join()
