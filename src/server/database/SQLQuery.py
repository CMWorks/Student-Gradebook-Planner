import sqlite3
from database.dbQuery import DbQuery
from database.SQLConnection import SQLConnection


class SQLQuery(DbQuery):

    db = None

    def __data_to_dict(self, data) -> list:
        out = []
        for row in data:
            out.append(row)
        
        return out

    @staticmethod
    def getDbQuery(path:str):
        if SQLQuery.db is None:
            SQLQuery.db = SQLQuery(path)
        return SQLQuery.db

    def __init__(self, path):
        self.dbConnect = SQLConnection(path)
        self.isOpen = True


    # Awful way to fix cross threads, but it works.
    def get(self, table, id_name, id):
        while True:
            try:
                self.conn = self.dbConnect.connect()
                data = self.conn.execute(
                    f"select * from {table} where {id_name}='{id}'")
                return self.__data_to_dict(data)
            except Exception:
                print("Error - retrying select command")

    def add(self, table, dicData: dict):
        self.conn = self.dbConnect.connect()
        id_str = '('
        value_str = '('
        for key, value in dicData.items():
            id_str += f"{key},"
            value_str += f"'{value}',"

        # remove the last comma and add ending )
        id_str = id_str[:-1] + ")"
        value_str = value_str[:-1] + ")"

        command = f"insert into {table} {id_str} values {value_str};"

        try:
            self.conn.execute(command)
        except sqlite3.IntegrityError as e:
            print(e)
            self.conn.close()
            return False

        out = True
        if self.conn.total_changes == 0:
            out = False
        self.conn.commit()
        self.conn.close()
        return out

    def update(self, table, dicData: dict, id_name, id):
        self.conn = self.dbConnect.connect()
        command = f"update {table} set "
        for key, value in dicData.items():
            command += f"{key} = '{value}',"

        # remove the last comma and add ending )
        command = command[:-1] + f" where {id_name} = '{id}'"

        try:
            self.conn.execute(command)
        except sqlite3.IntegrityError as e:
            print(e)
            self.conn.close()
            return False
        out = True
        if self.conn.total_changes == 0:
            out = False
        self.conn.commit()
        self.conn.close()
        return out

    def delete(self, table, id_name, id):
        self.conn = self.dbConnect.connect()
        try:
            self.out = self.conn.execute(f"delete from {table} where {id_name}='{id}'")
        except sqlite3.IntegrityError as e:
            print(e)
            self.conn.close()
            return False
        out = True
        if self.conn.total_changes == 0:
            out = False
        self.conn.commit()
        self.conn.close()
        return out