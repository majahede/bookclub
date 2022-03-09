import csv

def parse_books_csv():
  file = open('./data/books.csv')
  books_data = csv.reader(file)
  next(books_data)
  all_books = []
  for row in books_data:
    value = [row[0], row[1], row[2],  row[3],  row[4],  row[5]]
    all_books.append(value)
  return all_books

def parse_members_csv():
  file = open('./data/members.csv')
  members_data = csv.reader(file)
  next(members_data)
  all_members = []
  for row in members_data:
    value = [row[0], row[1], row[2],  row[3]]
    all_members.append(value)
  return all_members

def parse_reviews_csv():
  file = open('./data/reviews.csv')
  reviews_data = csv.reader(file)
  next(reviews_data)
  all_reviews = []
  for row in reviews_data:
    value = [row[0], row[1], row[2]]
    all_reviews.append(value)
  return all_reviews