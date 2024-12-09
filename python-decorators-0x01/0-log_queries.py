import sqlite3
import functools
from datetime import datetime
#### decorator to log SQL queries

def log_queries(func):
    """ Decorator to log SQL queries before executing them
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log the SQL query
        if args:
            print(f"{datetime.now()}: Executing SQL query: {args[0]}")
        # Call the original function
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")