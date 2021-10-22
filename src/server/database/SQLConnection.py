import sqlite3

from database.dbConnection import DbConnection


class SQLConnection(DbConnection):
    def __init__(self):
        self.conn = None

    def connect(self, path):
        self.conn = None
        f = open(path)
        d = f.read().split('=')
        f.close()
        # if d[0] == 'location' and len(d) == 2:
        self.conn = sqlite3.connect(d[1])

        # Ensures that the cascade constraint is enforced
        self.conn.execute("PRAGMA foreign_keys = 1")
        return self.conn

    def close(self):
        self.conn.close()
