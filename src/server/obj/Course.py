from database.dbQuery import DbQuery


class Course:
    def __init__(self, db: DbQuery, dictData: dict = None):
        self.db = db
        if dictData is None:
            self.courseID = -1
            self.courseName = ''
            self.creditHours = 0
            self.courseType = None
            self.userID = ''
        else:
            self.courseID = dictData['courseID']
            self.courseName = dictData['courseName']
            self.creditHours = dictData['creditHours']
            self.courseType = None
            self.userID = dictData['userID']

    @staticmethod
    def getCourses(db: DbQuery, id):
        raise NotImplementedError

    @staticmethod
    def deleteCourses(db: DbQuery, idName, id):
        raise NotImplementedError

    def addCourse(self):
        raise NotImplementedError

    def updateCourse(self):
        raise NotImplementedError

    def getCourseID(self):
        return self.courseID

    def getCourseName(self):
        return self.courseName

    def getCreditHours(self):
        return self.creditHours

    def getUserID(self):
        return self.userID

    def setCourseID(self, id):
        self.courseID = id

    def setCourseName(self, name):
        self.courseName = name

    def setCreditHours(self, hours):
        self.creditHours = hours

    def setUserID(self, id):
        self.userID = id