from database.dbQuery import DbQuery


class DbHandler:
    @staticmethod
    def get(db: DbQuery, idName: str, id):
        raise NotImplementedError

    @staticmethod
    def delete(db: DbQuery, idName: str, id) -> bool:
        raise NotImplementedError

    @staticmethod
    def add(db: DbQuery, obj: object) -> bool:
        raise NotImplementedError

    @staticmethod
    def update(db: DbQuery, obj: object) -> bool:
        raise NotImplementedError
