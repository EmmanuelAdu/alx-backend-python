import mysql.connector
from mysql.connector import Error
import uuid
import csv


''' Function to connect to mysql database server
'''

def connect_db():
    try:
        connection = mysql.connector.connect(
            user='root',
            host='localhost',
            port='33061',
            password='new_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None



''' Function to create ALX_prodev database if it doesn't exist
'''
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print('Database created successfully or Database already exist')
    except Error as e:
        print(f"Error creating database: {e}")



''' Function to connect to database prodev
'''
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='new_password',
            database='ALX_prodev',
            port='33061'
        )
        if connection.is_connected():
            print('Successfully connected to database')
            return connection
    except Error as e:
        print(f"Error while connecting to ALX_prodev: {e}")
        return None


''' Function to create user_table if it doesn't exist
'''
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data(
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL
            );
        ''')
        print('Table user created successfully')
    except Error as e:
        print(f"Error create user table: {e}")


''' Function to insert data into the user_data table
'''
def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        with open(data, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
                cursor.execute(
                    '''
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email), age=VALUES(age);
                    ''',
                    (user_id, name, email, age)
                )
        connection.commit()
        print('Data inserted successfully')
    except Error as e:
        print(f"Error while inserting data: {e}")
    except FileNotFoundError:
        print(f"File {data} not found")