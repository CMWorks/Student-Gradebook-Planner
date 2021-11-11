from obj.DbHandler import DbHandler
from database.dbQuery import DbQuery
from obj.User import User


class UserDbHandler(DbHandler):

    _tabel_name = 'STUDENT'

    @staticmethod
    def get(db: DbQuery, idName: str, id: str) -> User:
        try:
            userData = db.get(UserDbHandler._tabel_name, 'userID', id)
            if len(userData) != 1:
                return None
            data = UserDbHandler.toJson(userData[0])
            new_user = User(data)
        except Exception:
            return None

        return new_user

    @staticmethod
    def delete(db: DbQuery, idName: str, id) -> bool:
        try:
            return db.delete(UserDbHandler._tabel_name, 'userID', id)
        except Exception:
            return False

    @staticmethod
    def add(db: DbQuery, obj: User) -> bool:
        try:
            dictData = obj.toJson()
            return db.add(UserDbHandler._tabel_name, dictData)
        except Exception:
            return False

    @staticmethod
    def update(db: DbQuery, obj: User) -> bool:
        try:
            dictData = obj.toJson()
            return db.update(UserDbHandler._tabel_name, dictData, 'userID', obj.getUserID())
        except Exception:
            return False

    @staticmethod
    def toJson(array):
        data = {'userID': array[0],
                'firstName': array[1],
                'lastName': array[2],
                'email': array[3],
                'totalGPA': array[4]
                }

        return data
