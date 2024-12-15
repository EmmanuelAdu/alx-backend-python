import sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, params=()):
        """Initialize with database name, query and parameter
        """
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.results = None

    def __enter__(self):
        """Connect to database and perform query
        """

        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Ensure database is properly closed
        """
        if self.connection:
            self.connection.commit()
            self.connection.close()