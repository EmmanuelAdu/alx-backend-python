import mysql.connector
from mysql.connector import Error


def connect_to_database():
    """ Function to connect to mysql database ALX_prodev
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
            print("Successfully connected to ALX_prodev")
            return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None


def stream_users_in_batches(batch_size):
    """Generator function to fetch data in batches
    """
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch
    
    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """ Processes users in batches, filtering for users 
        over the age of 25
    """
    for batch in stream_users_in_batches(batch_size):
        processed_batch = [user for user in batch if user['age'] > 25]
        for user in processed_batch:
            print(user)