import mysql.connector
from mysql.connector import errorcode
import parsefiles

connect_error = "Failed to connect"
table_error = "Failed to create table"
insert_error = "Failed to insert"


def connect_database(user, password, host, db_name):
    try:
        cnx = mysql.connector.connect(user=user, password=password, host=host)
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        print("{} {}".format(connect_error, err))
        exit(1)

    try:
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        if is_not_database_missing_error(err):
            print("{} {}".format(connect_error, err))
            exit(1)

        print("Database does not exist. Creating new database...")
        create_database(cursor, db_name)
        cursor.execute("USE {}".format(db_name))

    return cnx


def is_not_database_missing_error(err):
    return err.errno != errorcode.ER_BAD_DB_ERROR


def create_database(cursor, db_name):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        print("Database '{}' was created succesfully.".format(db_name))
    except mysql.connector.Error as err:
        print("Failed to create database {}".format(err))
        exit(1)


def drop_table(cursor, table_name):
    try:
        cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    except mysql.connector.Error as err:
        print("Failed to drop table {}".format(err))
        exit(1)


def create_books_table(cursor):
    try:
        cursor.execute("CREATE TABLE books (book_id int not null, title nvarchar(200), author nvarchar(200), genre nvarchar(200), publisher nvarchar(200), year int, primary key(book_id))")
    except mysql.connector.Error as err:
        print("{} {}".format(table_error, err))
        exit(1)


def create_members_table(cursor):
    try:
        cursor.execute(
            "CREATE TABLE members (member_id int not null, name nvarchar(200), age int, city nvarchar(200), primary key(member_id))")
    except mysql.connector.Error as err:
        print("{} {}".format(table_error, err))
        exit(1)


def create_reviews_table(cursor):
    try:
        cursor.execute(
            "CREATE TABLE reviews (member_id int not null, book_id int not null, rating int, primary key(member_id, book_id))")
    except mysql.connector.Error as err:
        print("{} {}".format(table_error, err))
        exit(1)


def insert_books(cursor):
    try:
        cursor.executemany(
            "INSERT INTO books (`book_id`, `title` ,`author`,`genre`,`publisher`,`year`) values (%s, %s, %s, %s, %s, %s)", parsefiles.parse_books_csv())
    except mysql.connector.Error as err:
        print("{} {}".format(insert_error, err))
        exit(1)


def insert_members(cursor):
    try:
        cursor.executemany(
            "INSERT INTO members (`member_id`, `name` ,`age`,`city`) values (%s, %s, %s, %s)", parsefiles.parse_members_csv())
    except mysql.connector.Error as err:
        print("{} {}".format(insert_error, err))
        exit(1)


def insert_reviews(cursor):
    try:
        cursor.executemany(
            "INSERT INTO reviews (`member_id` ,`book_id`,`rating`) values (%s, %s, %s)", parsefiles.parse_reviews_csv())
    except mysql.connector.Error as err:
        print("{} {}".format(insert_error, err))
        exit(1)
