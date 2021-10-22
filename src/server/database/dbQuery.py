class DbQuery:

    db = None

    @staticmethod
    def getDbQuery():
        raise NotImplementedError

    def __init__(self):
        raise NotImplementedError

    def get(self, table, id_name, id) -> list:
        raise NotImplementedError

    def add(self, table, listData:list) -> bool:
        raise NotImplementedError

    def update(self, table, dicData:dict) -> bool:
        raise NotImplementedError

    def delete(self, table, id_name, id) -> bool:
        raise NotImplementedError