def list_books(cursor):
    cursor.execute("""SELECT * 
                      FROM books""")

    print("| {:<5} | {:<35} | {:<25} | {:<25} | {:<10} | {}".format(
        "id", "title", "author", "genre", "publisher", "year"))
    print("-"*124)

    for (book_id, title, author, genre, publisher, year) in cursor:
        print("| {:<5} | {:<35} | {:<25} | {:<25} | {:<10} |  {}".format(
            book_id, title, author, genre, publisher, year))


def list_books_from_author(cursor, author):
    cursor.execute("""SELECT book_id, title, genre, publisher, year 
                      FROM books 
                      WHERE author='{}'""".format(author))

    print(author)
    print("-"*124)

    print("| {:<5} | {:<35} | {:<25} | {:<10} | {}".format(
        "id", "title", "genre", "publisher", "year"))
    print("-"*124)

    for (book_id, title, genre, publisher, year) in cursor:
        print("| {:<5} | {:<35} | {:<25} | {:<10} |  {}".format(
            book_id, title, genre, publisher, year))


def average_rating_book(cursor, book):
    cursor.execute(
        """SELECT books.title, AVG(reviews.rating) 
           FROM books 
           JOIN reviews on books.book_id = reviews.book_id 
           WHERE title='{}'""".format(book))

    print("-"*60)

    for (title, rating) in cursor:
        if title == None:
            print("The book does not exist!")
            return
        print("{} has an average rating of {}".format(title, round(rating, 1)))


def average_rating_writer(cursor, author):
    cursor.execute(
        """SELECT books.author, AVG(reviews.rating) 
           FROM books 
           JOIN reviews on books.book_id = reviews.book_id 
           WHERE author='{}'""".format(author))

    print("-"*60)

    for (author, rating) in cursor:
        if author == None:
            print("The author does not exist!")
            return
        print("{} has an average rating of {}".format(author, round(rating, 1)))


def most_popular_book(cursor, city):
    cursor.execute(fetch_popular_book("MAX(avg)", city, ""))

    max_avg = 0
    for (rating) in cursor:
        max_avg = rating[0]
    
    if max_avg != None:
        cursor.execute(fetch_popular_book(
            "*", city, "WHERE avg >= {}".format(max_avg)))

    if max_avg != None:
        print("| Most popular book[s] in {}".format(city))
        print("-"*60)

        print("| {:<40} | {}".format(
            "Title", "Average rating"))
        print("-"*60)

        for (title, rating) in cursor:
            print("| {:<40} | {}".format(
                title, rating))
    else:
        print("No books found!")


def fetch_popular_book(selector, city, where):
    return """
            SELECT {}
            FROM (
                SELECT 
                    books.title,
                    AVG(reviews.rating) as avg
                FROM
                    books
                JOIN reviews
                    ON books.book_id = reviews.book_id
                JOIN members
                    ON reviews.member_id = members.member_id
                WHERE city = '{}'
                GROUP BY books.title
                ORDER BY avg DESC
            ) tmp
            {}
            """.format(selector, city, where)

def list_member_by_reviews(cursor):
    cursor.execute(
        """SELECT members.name, COUNT(reviews.rating)
           FROM reviews
           JOIN members on reviews.member_id = members.member_id
           GROUP BY reviews.member_id
           Order BY COUNT(reviews.rating) DESC 
           """)

    print("-"*60)
    print("| {:<30} | {}".format(
        "Name", "Number of books reviewed"))
    print("-"*60)

    for x in cursor:
        print("| {:<30} | {}".format(
            x[0], x[1]))


def list_members_books(cursor, member):
    cursor.execute(
        """SELECT books.title, books.author
           FROM books
           JOIN reviews on reviews.book_id = books.book_id
           JOIN members on members.member_id = reviews.member_id
           WHERE members.name = '{}'
           """.format(member))
    
    print("| Books reviewed by {}".format(member))
    print("-"*80)

    print("| {:<40} | {}".format(
        "Title", "Author"))
    print("-"*80)

    for (title, author) in cursor:
        print("| {:<40} | {}".format(
            title, author))


def author_view(cursor, author):
    cursor.execute("DROP VIEW IF EXISTS author")
    cursor.execute(
        """CREATE VIEW author as SELECT title, year 
           FROM books 
           WHERE author ='{}'""".format(author))

    cursor.execute("""SELECT * 
                      FROM author""")

    print(author)
    print("-"*60)
    print("| {:<35} |  {}".format(
        "title", "year"))
    print("-"*60)
    for (title, year) in cursor:
        print("| {:<35} |  {}".format(title,  year))
