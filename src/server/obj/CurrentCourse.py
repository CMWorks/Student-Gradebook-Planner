from obj.Course import Course
from database.dbQuery import DbQuery
from obj.Category import Category


class CurrentCourse(Course):

    _tabel_name = "CURRENT_COURSE"

    def __init__(self, db: DbQuery, dictData: dict = None):
        super().__init__(db, dictData)
        if dictData is None:
            self.isOnline = False
            self.grade = 0.0
            self.semesterID = 0
        else:
            self.isOnline = dictData['isOnline']
            self.grade = dictData['grade']
            self.semesterID = dictData['semesterID']

    @staticmethod
    def getCourses(db: DbQuery, idName, id):
        courseData = db.get(CurrentCourse._tabel_name, idName, id)
        
        out:list[CurrentCourse] = []
        for data in courseData:
            id = data[0]
            name = data[1]
            hours = data[2]
            online = data[3]
            grade = data[4]
            sid = data[5]
            uid = data[6]
            new_course = CurrentCourse(db)
            new_course.setCourseID(id)
            new_course.setCourseName(name)
            new_course.setCreditHours(hours)
            new_course.setIsOnline(online)
            new_course.setGrade(grade)
            new_course.setSemesterID(sid)
            new_course.setUserID(uid)
            out.append(new_course)

        return out

    @staticmethod
    def deleteCourses(db: DbQuery, idName, id):
        return db.delete(CurrentCourse._tabel_name, idName, id)

    def addCourse(self):
        dictData = self.toJson()
        return self.db.add(CurrentCourse._tabel_name, dictData)

    def updateCourse(self):
        dictData = self.toJson()
        return self.db.update(CurrentCourse._tabel_name, dictData, 'courseID', self.getCourseID())

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

    def updateGrade(self):
        categories = Category.getCategories(self.db, 'courseID', self.courseID)

        if len(categories) == 0:
            self.setGrade(0)
            return

        total = 0
        for category in categories:
            category.updateCategoryGrade()
            total += category.getCategoryGrade()*category.getWeight()
        self.setGrade(total)