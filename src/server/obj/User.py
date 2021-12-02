class User:
    def __checkType(self):
        if type(self.userID) != str or type(self.firstName) != str or type(self.lastName) != str or type(self.email) != str or (type(self.totalGPA) != float and type(self.totalGPA) != int):
            raise TypeError

    def __checkValue(self):
        if self.totalGPA < 0:
            raise ValueError

    def __init__(self, dictData: dict):
        self.userID: str = dictData['userID']
        self.firstName: str = dictData['firstName']
        self.lastName: str = dictData['lastName']
        self.email: str = dictData['email']
        self.totalGPA: float = dictData['totalGPA']
        self.__checkType()
        self.__checkValue()

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
        data = {'userID': self.getUserID(),
                'firstName': self.getFirstName(),
                'lastName': self.getLastName(),
                'email': self.getEmail(),
                'totalGPA': self.getTotalGPA()
                }

        return data
