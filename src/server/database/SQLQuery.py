import sqlite3
from database.dbQuery import DbQuery
from database.SQLConnection import SQLConnection


class SQLQuery(DbQuery):

    db = None

    def __data_to_dict(self, data):
        out = []
        for row in data:
            out.append(row)
        self.conn.close()
        return out

    @staticmethod
    def getDbQuery(path):
        if SQLQuery.db is None:
            SQLQuery.db = SQLQuery(path)
        return SQLQuery.db

    def __init__(self, path):
        self.dbConnect = SQLConnection()
        self.path = path
        self.isOpen = True

    def get(self, table, id_name, id):
        self.conn = self.dbConnect.connect(self.path)
        data = self.conn.execute(
            f"select * from {table} where {id_name}='{id}'")
        return self.__data_to_dict(data)

    def add(self, table, listData: list):
        self.conn = self.dbConnect.connect(self.path)
        command = f"insert into {table} values("
        for value in listData:
            command += f"'{value}',"

        # remove the last comma and add ending )
        command = command[:-1] + ")"

        try:
            self.conn.execute(command)
        except sqlite3.IntegrityError:
            self.conn.close()
            return False
        self.conn.commit()
        self.conn.close()
        return True

    def update(self, table, dicData: dict):
        self.conn = self.dbConnect.connect(self.path)
        command = f"update {table} set "
        for key, value in dicData.items():
            command += f"{key} = '{value}',"

        # remove the last comma and add ending )
        command = command[:-1]

        try:
            self.conn.execute(command)
        except sqlite3.IntegrityError:
            self.conn.close()
            return False
        self.conn.commit()
        self.conn.close()
        return True

    def delete(self, table, id_name, id):
        self.conn = self.dbConnect.connect(self.path)
        try:
            self.conn.execute(f"delete from {table} where {id_name}='{id}'")
        except sqlite3.IntegrityError:
            self.conn.close()
            return False
        self.conn.commit()
        self.conn.close()
        return True
