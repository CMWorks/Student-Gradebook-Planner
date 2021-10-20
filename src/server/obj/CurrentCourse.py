from obj.Course import Course
from database.dbQuery import DbQuery
from obj.Category import Category


class CurrentCourse(Course):

    _tabel_name = "CurrentCourse"

    def __init__(self, db: DbQuery, dictData: dict = None):
        super().__init__(db, dictData)
        if dictData is None:
            self.isOnline = False
            self.grade = 0.0
        else:
            self.isOnline = dictData['isOnline']
            self.grade = dictData['grade']

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
            new_course = CurrentCourse(db)
            new_course.setCourseID(id)
            new_course.setCourseName(name)
            new_course.setCredditHours(hours)
            new_course.setIsOnline(online)
            new_course.setGrade(grade)
            out.append(new_course)

        return out

    @staticmethod
    def deleteCourses(db: DbQuery, idName, id):
        return db.delete(CurrentCourse._tabel_name, idName, id)

    def addCourse(self):
        listData = [self.getCourseID(), self.getCourseName(), self.getCredditHours(), self.getIsOnline(), self.getGrade()]
        return self.db.add(CurrentCourse._tabel_name, listData)

    def updateCourse(self):
        dictData = self.toJson()
        return self.db.update(CurrentCourse._tabel_name, dictData)

    def getIsOnline(self):
        return self.isOnline

    def getGrade(self):
        return self.grade

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

    def toJson(self):
        data = {'courseID':self.getCourseID(),
                'courseName': self.getCourseName(),
                'creditHours': self.getCredditHours(),
                'isOnline': self.getIsOnline(),
                'grade': self.getGrade()
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