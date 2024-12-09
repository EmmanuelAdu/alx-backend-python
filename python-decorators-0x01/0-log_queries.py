import sqlite3
import functools

#### decorator to log SQL queries

def log_queries():
    """ Decorator to log SQL queries before executing them
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log the SQL query
            if args:
                print(f"Executing SQL query: {args[0]}")
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator


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