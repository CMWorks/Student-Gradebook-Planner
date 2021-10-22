from database.dbQuery import DbQuery
from obj.Assignment import Assignment


class Category:

    _tabel_name = 'CATEGORIES'

    def __init__(self, db: DbQuery, dictData: dict = None):
        if dictData is None:
            self.db = db
            self.categoryID = -1
            self.categoryName = ''
            self.weight = 1
            self.categoryGrade = 0.0
            self.courseID = 0
            self.semesterID = 0
            self.userID = 0
        else:
            self.db = db
            self.categoryID = dictData['categoryID']
            self.categoryName = dictData['categoryName']
            self.weight = dictData['weight']
            self.categoryGrade = dictData['categoryGrade']
            self.courseID = dictData['courseID']
            self.semesterID = dictData['semesterID']
            self.userID = dictData['userID']

    @staticmethod
    def getCategories(db: DbQuery, idName, id):
        categoryData = db.get(Category._tabel_name, idName, id)
        
        out:list[Category] = []
        for data in categoryData:
            id = data[0]
            name = data[1]
            weight = data[2]
            grade = data[3]
            coid = data[4]
            sid = data[5]
            uid = data[6]
            new_category = Category(db)
            new_category.setCategoryID(id)
            new_category.setCategoryName(name)
            new_category.setWeight(weight)
            new_category.setCategoryGrade(grade)
            new_category.setCourseID(coid)
            new_category.setSemesterID(sid)
            new_category.setUserID(uid)
            out.append(new_category)

        return out

    @staticmethod
    def deleteCategories(db: DbQuery, idName, id):
        return db.delete(Category._tabel_name, idName, id)

    def addCategory(self):
        dictData = self.toJson()
        return self.db.add(Category._tabel_name, dictData)

    def updateCategory(self):
        dictData = self.toJson()
        return self.db.update(Category._tabel_name, dictData, 'categoryID', self.getCategoryID())

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

    def updateCategoryGrade(self):
        assignments = Assignment.getAssignments(self.db, 'categoryID', self.categoryID)

        if len(assignments) == 0:
            self.setCategoryGrade(0)
            return

        total = 0
        for assignment in assignments:
            total += assignment.getPercentGrade()
        self.setCategoryGrade(total/len(assignments))