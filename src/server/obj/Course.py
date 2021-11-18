class Course:
    def __init__(self, dictData: dict = None):
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
        
    def toJson(self) -> dict:
        raise NotImplementedError