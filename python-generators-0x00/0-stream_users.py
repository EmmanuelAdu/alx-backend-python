import mysql.connector
from mysql.connector import Error


def stream_users():
    """
    Generator function to stream rows from SQL user_data table
    """
    try:
        connection = mysql.connector.connect(
        user='root',
        host='localhost',
        password='new_password',
        port='33061',
        database='ALX_prodev'
        )
        if connection:
            cursor = connection.cursor(dictionary=True) # Fetch rows as dictionary
            cursor.execute("SELECT * FROM user_data")

            for row in cursor:
                yield row
    except Error as e:
        print(f"Error fetching data: {e}")