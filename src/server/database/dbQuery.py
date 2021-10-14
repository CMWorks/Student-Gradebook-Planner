class DbQuery:

    db = None

    @staticmethod
    def getDbQuery():
        raise NotImplementedError

    def __init__(self):
        raise NotImplementedError

    def get(self, table, id_name, id):
        raise NotImplementedError

    def add(self, table, data):
        raise NotImplementedError

    def update(self, table, data):
        raise NotImplementedError

    def delete(self, table, id_name, id):
        raise NotImplementedError