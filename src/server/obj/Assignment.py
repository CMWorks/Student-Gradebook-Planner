class Assignment:

    def __init__(self, dictData: dict = None):
        if dictData is None:
            self.assignmentID = -1
            self.assignmentName = ''
            self.pointsReceived = 0.0
            self.totalPoints = 0.0
            self.percentGrade = 0.0
            self.dueDate = None
            self.isDone = False
            self.categoryID = 0
            self.courseID = 0
            self.semesterID = 0
            self.userID = 0
        else:
            self.assignmentID = dictData['assignmentID']
            self.assignmentName = dictData['assignmentName']
            self.pointsReceived = float(dictData['pointsReceived'])
            self.totalPoints = float(dictData['totalPoints'])
            self.percentGrade = float(dictData['percentGrade'])
            self.dueDate = dictData['dueDate']
            self.isDone = bool(dictData['isDone'])
            self.categoryID = dictData['categoryID']
            self.courseID = dictData['courseID']
            self.semesterID = dictData['semesterID']
            self.userID = dictData['userID']

    def calculateGrade(self):
        if self.totalPoints <= 0.01:
            self.percentGrade = 0
        self.percentGrade = 100.0 * self.pointsReceived / self.totalPoints

    def getAssignmentID(self):
        return self.assignmentID

    def getAssignmentName(self):
        return self.assignmentName

    def getPointsReceived(self):
        return self.pointsReceived

    def getTotalPoints(self):
        return self.totalPoints

    def getPercentGrade(self):
        return self.percentGrade

    def getIsDone(self):
        return self.isDone

    def getDueDate(self):
        return self.dueDate

    def getCategoryID(self):
        return self.categoryID

    def getCourseID(self):
        return self.courseID

    def getSemesterID(self):
        return self.semesterID

    def getUserID(self):
        return self.userID

    def setAssignmentID(self, id):
        self.assignmentID = id

    def setAssignmentName(self, name):
        self.assignmentName = name

    def setPointsReceived(self, points):
        self.pointsReceived = points

    def setTotalPoints(self, total):
        self.totalPoints = total

    def setPercentGrade(self, grade):
        self.percentGrade = grade

    def setIdDone(self, done):
        self.isDone = done

    def setCategoryID(self, id):
        self.categoryID = id

    def setCourseID(self, id):
        self.courseID = id

    def setSemesterID(self, id):
        self.semesterID = id

    def setUserID(self, id):
        self.userID = id

    def toJson(self):
        data = {'assignmentID':self.getAssignmentID(),
                'assignmentName': self.getAssignmentName(),
                'pointsReceived': self.getPointsReceived(),
                'totalPoints': self.getTotalPoints(),
                'percentGrade': self.getPercentGrade(),
                'dueDate': self.getDueDate(),
                'isDone': int(self.getIsDone()),
                'categoryID': self.getCategoryID(),
                'courseID': self.getCourseID(),
                'semesterID': self.getSemesterID(),
                'userID': self.getUserID()
                }
        return data

    def setDueDate(self, due):
        self.dueDate = due
