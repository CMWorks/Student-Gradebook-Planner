from obj.Course import Course
from database.dbQuery import DbQuery


class FutureCourse(Course):

    _tabel_name = 'FUTURE_COURSE'

    def __init__(self, db: DbQuery, dictData: dict = None):
        super().__init__(db, dictData)
        if dictData is None:
            self.plannedSemester = ""
        else:
            self.plannedSemester = dictData['plannedSemester']

    @staticmethod
    def getCourses(db: DbQuery, idName, id):
        courseData = db.get(FutureCourse._tabel_name, idName, id)
        
        out:list[FutureCourse] = []
        for data in courseData:
            id = data[0]
            name = data[1]
            hours = data[2]
            plan = data[3]
            uid = data[4]
            new_course = FutureCourse(db)
            new_course.setCourseID(id)
            new_course.setCourseName(name)
            new_course.setCreditHours(hours)
            new_course.setPlannedSemester(plan)
            new_course.setUserID(uid)
            out.append(new_course)

        return out

    @staticmethod
    def deleteCourses(db: DbQuery, idName, id):
        return db.delete(FutureCourse._tabel_name, idName, id)

    def addCourse(self):
        dictData = self.toJson()
        return self.db.add(FutureCourse._tabel_name, dictData)

    def updateCourse(self):
        dictData = self.toJson()
        return self.db.update(FutureCourse._tabel_name, dictData, 'courseID', self.getCourseID())

    def getPlannedSemester(self):
        return self.plannedSemester

    def setPlannedSemester(self, sem):
        self.plannedSemester = sem

    def toJson(self):
        data = {'courseID':self.getCourseID(),
                'courseName': self.getCourseName(),
                'creditHours': self.getCreditHours(),
                'plannedSemester': self.getPlannedSemester(),
                'userID': self.getUserID()
                }
        return data