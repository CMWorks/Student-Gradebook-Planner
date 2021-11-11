import sqlite3

from database.dbConnection import DbConnection


class SQLConnection(DbConnection):
    def __init__(self, path):
        self.conn = None

        f = open(path)
        dbase = f.read().split('=')[1]
        f.close()
        print(f'Connected to {dbase}')
        self.path = dbase

    def connect(self):
        self.conn = None
        # if d[0] == 'location' and len(d) == 2:
        self.conn = sqlite3.connect(self.path)

        # Ensures that the cascade constraint is enforced
        self.conn.execute("PRAGMA foreign_keys = 1")
        # self.conn.execute("PRAGMA JOURNAL_MODE = 'WAL'")
        return self.conn

    def close(self):
        self.conn.close()
