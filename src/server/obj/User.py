from typing import overload
from database.dbQuery import DbQuery
from obj.Semester import Semester


class User:
    _tabel_name = 'STUDENT'

    def __init__(self, db: DbQuery, dictData: dict = None):
        if dictData is None:
            self.db = db
            self.userID = ''
            self.firstName = ''
            self.lastName = ''
            self.email = ''
            self.totalGPA = 0.0
        else:
            self.db = db
            self.userID = dictData['userID']
            self.firstName = dictData['firstName']
            self.lastName = dictData['lastName']
            self.email = dictData['email']
            self.totalGPA = dictData['totalGPA']

    @staticmethod
    def getUser(db: DbQuery, id):
        userData = db.get(User._tabel_name, 'userID', id)
        if len(userData) != 1:
            return None
        
        userData = userData[0]
        id = userData[0]
        first = userData[1]
        last = userData[2]
        email = userData[3]
        gpa = userData[4]
        new_user = User(db)
        new_user.setUserID(id)
        new_user.setFirstName(first)
        new_user.setLastName(last)
        new_user.setEmail(email)
        new_user.setTotalGPA(gpa)

        return new_user

    @staticmethod
    def deleteUser(db: DbQuery, id):
        return db.delete(User._tabel_name, 'userID', id)

    def addUser(self):
        dictData = self.toJson()
        return self.db.add(User._tabel_name, dictData)

    def updateUser(self) -> bool:
        dictData = self.toJson()
        return self.db.update(User._tabel_name, dictData, 'userID', self.getUserID())

    def getUserID(self):
        return self.userID

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def getTotalGPA(self):
        return self.totalGPA

    def setUserID(self, id):
        self.userID = id

    def setFirstName(self, name):
        self.firstName = name

    def setLastName(self, name):
        self.lastName = name

    def setEmail(self, email):
        self.email = email

    def setTotalGPA(self, gpa):
        self.totalGPA = gpa

    def toJson(self):
        data = {'userID':self.getUserID(),
                'firstName': self.getFirstName(),
                'lastName': self.getLastName(),
                'email': self.getEmail(),
                'totalGPA': self.getTotalGPA()
        }

        return data

    def updateGPA(self):
        semesters = Semester.getSemesters(self.db, 'userID', self.userID)

        if len(semesters) == 0:
            self.setTotalGPA(0)
            return

        total = 0
        for sem in semesters:
            sem.updateGPA()
            total += sem.getGPA()
        self.setTotalGPA(total/len(semesters))