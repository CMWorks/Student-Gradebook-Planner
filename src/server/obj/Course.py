from database.dbQuery import DbQuery


class Course:
    def __init__(self, db: DbQuery, dictData: dict = None):
        if dictData is None:
            self.db = db
            self.courseID = -1
            self.courseName = ''
            self.creditHourse = 0
            self.courseType = None
        else:
            self.db = db
            self.courseID = dictData['courseID']
            self.courseName = dictData['courseName']
            self.creditHourse = dictData['creditHourse']
            self.courseType = None

    @staticmethod
    def getCourses(db: DbQuery, id):
        raise NotImplementedError

    def getCourseID(self):
        return self.courseID

    def getCourseName(self):
        return self.courseName

    def getCredditHours(self):
        return self.creditHourse

    def setCourseID(self, id):
        self.courseID = id

    def setCourseName(self, name):
        self.courseName = name

    def setCredditHours(self, hours):
        self.creditHourse = hours