import mysql.connector
import setup

cnx = mysql.connector.connect(user='root', password='root',
host='127.0.0.1', database='bookclub')
DB_NAME='bookclub'
cursor = cnx.cursor()

setup.create_database(cursor, DB_NAME)
setup.drop_table(cursor, 'books')
setup.drop_table(cursor, 'members')
setup.drop_table(cursor, 'reviews')
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