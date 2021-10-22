from database.dbQuery import DbQuery


class Assignment:

    _tabel_name = 'ASSIGNMENTS'

    def __init__(self, db: DbQuery, dictData: dict = None):
        if dictData is None:
            self.db = db
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
            self.db = db
            self.assignmentID = dictData['assignmentID']
            self.assignmentName = dictData['assignmentName']
            self.pointsReceived = dictData['pointsReceived']
            self.totalPoints = dictData['totalPoints']
            self.percentGrade = dictData['percentGrade']
            self.dueDate = dictData['dueDate']
            self.isDone = dictData['isDone']
            self.categoryID = dictData['categoryID']
            self.courseID = dictData['courseID']
            self.semesterID = dictData['semesterID']
            self.userID = dictData['userID']

    @staticmethod
    def getAssignments(db: DbQuery, idName, id):
        assData = db.get(Assignment._tabel_name, idName, id)
        
        out:list[Assignment] = []
        for data in assData:
            id = data[0]
            name = data[1]
            received = data[2]
            total = data[3]
            grade = data[4]
            due = data[5]
            done = data[6]
            caid = data[7]
            coid = data[8]
            sid = data[9]
            uid = data[10]
            new_assignment = Assignment(db)
            new_assignment.setAssignmentID(id)
            new_assignment.setAssignmentName(name)
            new_assignment.setPointsReceived(received)
            new_assignment.setTotalPoints(total)
            new_assignment.setPercentGrade(grade)
            new_assignment.setDueDate(due)
            new_assignment.setIdDone(done)
            new_assignment.setCategoryID(caid)
            new_assignment.setCourseID(coid)
            new_assignment.setSemesterID(sid)
            new_assignment.setUserID(uid)
            out.append(new_assignment)

        return out

    @staticmethod
    def deleteAssignments(db: DbQuery, idName, id):
        return db.delete(Assignment._tabel_name, idName, id)

    def addAssignment(self):
        dictData = self.toJson()
        return self.db.add(Assignment._tabel_name, dictData)

    def updateAssignment(self):
        dictData = self.toJson()
        return self.db.update(Assignment._tabel_name, dictData, 'assignmentID', self.getAssignmentID())

    def calculateGrade(self):
        if self.totalPoints <= 0.01:
            return None
        return self.pointsReceived / self.totalPoints

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
                'isDone': self.getIsDone(),
                'categoryID': self.getCategoryID(),
                'courseID': self.getCourseID(),
                'semesterID': self.getSemesterID(),
                'userID': self.getUserID()
                }
        return data

    def setDueDate(self, due):
        self.dueDate = due
