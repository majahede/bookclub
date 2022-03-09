def list_books(cursor):
    cursor.execute("SELECT * from books")
    for x in cursor:
        print(x)


def list_books_from_author(cursor):
    cursor.execute("SELECT title from books WHERE author='Lovell Norman'")
    for x in cursor:
        print(x[0])


def average_rating(cursor):
    cursor.execute(
        "SELECT title, AVG(stars) from books, reviews WHERE title = 'The Face of the Phoenix' ")
    for x in cursor:
        print(x[0] + " has the average rating of ", x[1])


def books_by_year(cursor):
    cursor.execute(
        "SELECT title, year from books WHERE year > 2015 ORDER BY year DESC")
    for x in cursor:
        print(x[0], x[1])


def average_age(cursor):
    cursor.execute("SELECT AVG(age) FROM members")
    for x in cursor:
        print(x[0])


def average_age_by_city(cursor):
    cursor.execute("SELECT city, AVG(age) FROM members GROUP BY city")
    for x in cursor:
        print(x[0], x[1])


def author_reviews(cursor):
    cursor.execute("SELECT members.name, reviews.stars, books.title from members, reviews, books WHERE books.book_id = reviews.book_id and reviews.member_id = members.member_id and books.author = 'Lovell Norman'")
    for x in cursor:
        print(x[0], x[1], x[2])


def join(cursor):
    cursor.execute(
        "SELECT members.name, reviews.stars from members JOIN reviews on members.member_id = reviews.member_id")
    for x in cursor:
        print(x)
