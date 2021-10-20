from database.dbQuery import DbQuery


class Assignment:

    _tabel_name = 'Assignment'

    def __init__(self, db: DbQuery, dictData: dict = None):
        if dictData is None:
            self.db = db
            self.assignmentID = -1
            self.assignmentName = ""
            self.pointsRecieved = 0.0
            self.totalPoints = 0.0
            self.percentGrade = 0.0
            self.dueDate = None
            self.isDone = False
        else:
            self.db = db
            self.assignmentID = dictData['assignmentID']
            self.assignmentName = dictData['assignmentName']
            self.pointsRecieved = dictData['pointsRecieved']
            self.totalPoints = dictData['totalPoints']
            self.percentGrade = dictData['percentGrade']
            self.dueDate = dictData['dueDate']
            self.isDone = dictData['isDone']

    @staticmethod
    def getAssignments(db: DbQuery, idName, id):
        assData = db.get(Assignment._tabel_name, idName, id)
        
        out:list[Assignment] = []
        for data in assData:
            id = data[0]
            name = data[1]
            recieved = data[2]
            total = data[3]
            grade = data[4]
            due = data[5]
            done = data[6]
            new_assignment = Assignment(db)
            new_assignment.setAssignmentID(id)
            new_assignment.setAssignmentName(name)
            new_assignment.setPointsRecieved(recieved)
            new_assignment.setTotalPoints(total)
            new_assignment.setPercentGrade(grade)
            new_assignment.setDueDate(due)
            new_assignment.setIdDone(done)
            out.append(new_assignment)

        return out

    @staticmethod
    def deleteAssignments(db: DbQuery, idName, id):
        return db.delete(Assignment._tabel_name, idName, id)

    def addAssignment(self):
        listData = [self.getAssignmentID(), self.getAssignmentName(), self.getPointsRecieved(), self.getTotalPoints(), self.getPercentGrade(), self.getDueDate(), self.getIsDone()]
        return self.db.add(Assignment._tabel_name, listData)

    def updateAssignment(self):
        dictData = self.toJson()
        return self.db.update(Assignment._tabel_name, dictData)

    def calculateGrade(self):
        if self.totalPoints <= 0.01:
            return None
        return self.pointsRecieved / self.totalPoints

    def getAssignmentID(self):
        return self.assignmentID

    def getAssignmentName(self):
        return self.getAssignmentName

    def getPointsRecieved(self):
        return self.pointsRecieved

    def getTotalPoints(self):
        return self.totalPoints

    def getPercentGrade(self):
        return self.percentGrade

    def getIsDone(self):
        return self.isDone

    def getDueDate(self):
        return self.dueDate

    def setAssignmentID(self, id):
        self.assignmentID = id

    def setAssignmentName(self, name):
        self.getAssignmentName = name

    def setPointsRecieved(self, points):
        self.pointsRecieved = points

    def setTotalPoints(self, total):
        self.totalPoints = total

    def setPercentGrade(self, grade):
        self.percentGrade = grade

    def setIdDone(self, done):
        self.isDone = done

    def toJson(self):
        data = {'assignmentID':self.getAssignmentID(),
                'assignmnetName': self.getAssignmentName(),
                'pointsRecieved': self.getPointsRecieved(),
                'totalPoints': self.getTotalPoints(),
                'percentGrade': self.getPercentGrade(),
                'dueDate': self.getDueDate(),
                'isDone': self.getIsDone
                }
        return data

    def setDueDate(self, due):
        self.dueDate = due
