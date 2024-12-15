import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        """Initialize with the database name"""
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """Establish database connection and return a cursor"""
        self.connection = sqlite3.connect(self.db_name)
        return self.connection.cursor()
    

    def __exit__(self, exc_type, exc_value):
        """Close the database connection"""
        if self.connection:
            self.connection.commit()
            self.connection.close()


if __name__ == "__main__":
    db_name = 'users.db'

    with DatabaseConnection(db_name) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for rows in results:
            print(rows)