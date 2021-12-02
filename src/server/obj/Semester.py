class Semester:
    def __init__(self, dictData: dict = None):
        if dictData is None:
            self.semesterID = -1
            self.semesterName = ''
            self.gpa = 0.0
            self.userID = ''
        else:
            self.semesterID = dictData['semesterID']
            self.semesterName = dictData['semesterName']
            self.gpa = dictData['gpa']
            self.userID = dictData['userID']

    def getSemesterID(self):
        return self.semesterID

    def getSemesterName(self):
        return self.semesterName

    def getGPA(self):
        return self.gpa

    def getUserID(self):
        return self.userID

    def setSemesterID(self, id):
        self.semesterID = id

    def setSemesterName(self, name):
        self.semesterName = name

    def setGPA(self, gpa):
        self.gpa = gpa

    def setUserID(self, id):
        self.userID = id

    def toJson(self):
        data = {'semesterID':self.getSemesterID(),
                'semesterName': self.getSemesterName(),
                'gpa': self.getGPA(),
                'userID': self.getUserID()
                }
        return data