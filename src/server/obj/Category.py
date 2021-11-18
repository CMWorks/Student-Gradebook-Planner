class Category:

    def __init__(self, dictData: dict = None):
        if dictData is None:
            self.categoryID = -1
            self.categoryName = ''
            self.weight = 1
            self.categoryGrade = 0.0
            self.courseID = 0
            self.semesterID = 0
            self.userID = 0
        else:
            self.categoryID = dictData['categoryID']
            self.categoryName = dictData['categoryName']
            self.weight = dictData['weight']
            self.categoryGrade = dictData['categoryGrade']
            self.courseID = dictData['courseID']
            self.semesterID = dictData['semesterID']
            self.userID = dictData['userID']

    def getCategoryName(self):
        return self.categoryName

    def getWeight(self):
        return self.weight

    def getCategoryGrade(self):
        return self.categoryGrade

    def getCategoryID(self):
        return self.categoryID

    def getCourseID(self):
        return self.courseID

    def getSemesterID(self):
        return self.semesterID

    def getUserID(self):
        return self.userID

    def setCategoryID(self, id):
        self.categoryID = id

    def setCategoryName(self, name):
        self.categoryName = name

    def setWeight(self, weight):
        self.weight = weight

    def setCategoryGrade(self, grade):
        self.categoryGrade = grade

    def setCourseID(self, id):
        self.courseID = id

    def setSemesterID(self, id):
        self.semesterID = id

    def setUserID(self, id):
        self.userID = id

    def toJson(self):
        data = {'categoryID':self.getCategoryID(),
                'categoryName': self.getCategoryName(),
                'weight': self.getWeight(),
                'categoryGrade': self.getCategoryGrade(),
                'courseID': self.getCourseID(),
                'semesterID': self.getSemesterID(),
                'userID': self.getUserID()
                }
        return data