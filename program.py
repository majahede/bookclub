import csv
from dataclasses import dataclass
import mysql.connector
import queries

cnx = mysql.connector.connect(user='root', password='root',
host='127.0.0.1', database='bookclub')
DB_NAME='bookclub'
cursor = cnx.cursor()

file = open('./data/books.csv')
books_data = csv.reader(file)
next(books_data)
all_books = []
for row in books_data:
  value = [row[0], row[1], row[2],  row[3],  row[4],  row[5]]
  all_books.append(value)

file = open('./data/members.csv')
members_data = csv.reader(file)
next(members_data)
all_members = []
for row in members_data:
  value = [row[0], row[1], row[2],  row[3]]
  all_members.append(value)

file = open('./data/reviews.csv')
reviews_data = csv.reader(file)
next(reviews_data)
all_reviews = []
for row in reviews_data:
  value = [row[0], row[1], row[2],  row[3]]
  all_reviews.append(value)

table_name = "reviews"
drop_table = "DROP TABLE IF EXISTS {}".format(table_name)

queries.create_database(cursor, DB_NAME)

create_books_table = "CREATE TABLE books (book_id int not null, title nvarchar(200), author nvarchar(200), genre nvarchar(200), publisher nvarchar(200), year int, primary key(book_id))"

create_members_table = "CREATE TABLE members (member_id int not null, name nvarchar(200), age int, city nvarchar(200), primary key(member_id))"

create_reviews_table = "CREATE TABLE reviews (review_id int not null, member_id int, book_id int, stars int, primary key(review_id))"

insert_books = "INSERT INTO books (`book_id`, `title` ,`author`,`genre`,`publisher`,`year`) values (%s, %s, %s, %s, %s, %s)"
insert_members = "INSERT INTO members (`member_id`, `name` ,`age`,`city`) values (%s, %s, %s, %s)"
insert_reviews = "INSERT INTO reviews (`review_id`, `member_id` ,`book_id`,`stars`) values (%s, %s, %s, %s)"

#cursor.execute(create_database)
#cursor.execute(drop_table)
#cursor.execute(create_books_table)
#cursor.execute(create_members_table)
#cursor.execute(create_reviews_table)
#cursor.executemany(insert_books, all_books)
#cursor.executemany(insert_members, all_members)
#cursor.executemany(insert_reviews, all_reviews)
#cnx.commit()
def list_books():
  cursor.execute("SELECT * from books")
  for x in cursor:
       print(x)

def list_books_from_author():
  cursor.execute("SELECT title from books WHERE author='Lovell Norman'")
  for x in cursor:
       print(x[0])

def average_rating():
  cursor.execute("SELECT title, AVG(stars) from books, reviews WHERE title = 'The Face of the Phoenix' ")
  for x in cursor:
      print(x[0] + " has the average rating of ", x[1])

def books_by_year():
  cursor.execute("SELECT title, year from books WHERE year > 2015 ORDER BY year DESC")
  for x in cursor:
      print(x[0], x[1])

def average_age():
  cursor.execute("SELECT AVG(age) FROM members")
  for x in cursor:
      print(x[0])

def average_age_by_city():
  cursor.execute("SELECT city, AVG(age) FROM members GROUP BY city")
  for x in cursor:
      print(x[0], x[1])

def author_reviews():
  cursor.execute("SELECT members.name, reviews.stars, books.title from members, reviews, books WHERE books.book_id = reviews.book_id and reviews.member_id = members.member_id and books.author = 'Lovell Norman'")
  for x in cursor:
      print(x[0], x[1], x[2])

def join():
  cursor.execute("SELECT members.name, reviews.stars from members JOIN reviews on members.member_id = reviews.member_id")
  for x in cursor:
      print(x)

# list_books()
# average_rating()
# list_books_from_author()
# books_by_year()
# average_age()
# average_age_by_city()
# author_reviews()
# join()