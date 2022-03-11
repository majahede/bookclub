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
    cursor.execute(
        """  
            SELECT MAX(avg)
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
        """.format(city))    

    max_avg = 0
    for (rating) in cursor:
        max_avg = rating[0]
    
    if max_avg != None:
        cursor.execute(
            """  
                SELECT *
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
                WHERE avg >= {}
            """.format(city, max_avg))

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


# def books_by_year(cursor):
#     cursor.execute(
#         "SELECT title, year from books WHERE year > 2015 ORDER BY year DESC")
#     for x in cursor:
#         print(x[0], x[1])

# def author_reviews(cursor):
#     cursor.execute("SELECT members.name, reviews.stars, books.title from members, reviews, books WHERE books.book_id = reviews.book_id and reviews.member_id = members.member_id and books.author = 'Lovell Norman'")
#     for x in cursor:
#         print(x[0], x[1], x[2])


# def join(cursor):
#     cursor.execute(
#         "SELECT members.name, reviews.rating from members JOIN reviews on members.member_id = reviews.member_id")
#     for x in cursor:
#         print(x)


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
