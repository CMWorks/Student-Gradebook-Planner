from obj.DbHandler import DbHandler
from database.dbQuery import DbQuery
from obj.User import User
from obj.SemesterDbHandler import SemesterDbHandler


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
            db.delete("CREDENTIALS", 'userID', id)
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
    
    def updateGPA(db, user: User):
        semesters = SemesterDbHandler.get(db, 'userID', user.getUserID())

        if len(semesters) == 0:
            user.setTotalGPA(4.0)
            UserDbHandler.update(db, user)
            return

        total = 0
        for sem in semesters:
            SemesterDbHandler.updateGPA(db, sem)
            total += sem.getGPA()
        user.setTotalGPA(total/len(semesters))
        UserDbHandler.update(db, user)
