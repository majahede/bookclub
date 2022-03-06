import csv
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
host='127.0.0.1')
DB_NAME='bookstore'
cursor = cnx.cursor()

def create_database(cursor, DB_NAME):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        print("Database created")
    except mysql.connector.Error as err:
        print("Faild to create database {}".format(err))
        exit(1)

create_database(cursor, DB_NAME)
