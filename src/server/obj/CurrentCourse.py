from obj.Course import Course


class CurrentCourse(Course):

    def __init__(self, dictData: dict = None):
        super().__init__(dictData)
        if dictData is None:
            self.isOnline = False
            self.grade = 0.0
            self.semesterID = 0
        else:
            self.isOnline = dictData['isOnline']
            self.grade = dictData['grade']
            self.semesterID = dictData['semesterID']

    def getIsOnline(self):
        return self.isOnline

    def getGrade(self):
        return self.grade

    def getSemesterID(self):
        return self.semesterID

    def getGPAGrade(self):
        if self.grade >= 90:
            return 4.0
        elif self.grade >= 80:
            return 3.0
        elif self.grade >= 70:
            return 2.0
        elif self.grade >= 60:
            return 1.0
        else:
            return 0.0

    def setGrade(self, grade):
        self.grade = grade

    def setIsOnline(self, online):
        self.isOnline = online

    def setSemesterID(self, id):
        self.semesterID = id

    def toJson(self):
        data = {'courseID':self.getCourseID(),
                'courseName': self.getCourseName(),
                'creditHours': self.getCreditHours(),
                'isOnline': self.getIsOnline(),
                'grade': self.getGrade(),
                'semesterID': self.getSemesterID(),
                'userID': self.getUserID()
                }
        return data