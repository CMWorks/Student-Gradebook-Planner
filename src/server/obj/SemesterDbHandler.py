from obj.DbHandler import DbHandler
from database.dbQuery import DbQuery
from obj.Semester import Semester
from obj.CourseDbHandler import CourseDbHandler
from obj.CurrentCourse import CurrentCourse


class SemesterDbHandler(DbHandler):

    _table_name = 'SEMESTER'

    @staticmethod
    def get(db: DbQuery, idName: str, id: str):
        new_objs: list[Semester] = []
        try:
            data_list = db.get(SemesterDbHandler._table_name, idName, id)
            for obj in data_list:
                data = SemesterDbHandler.toJson(obj)
                new_objs.append(Semester(data))
        except Exception:
            return []

        return new_objs

    @staticmethod
    def delete(db: DbQuery, idName: str, id) -> bool:
        try:
            return db.delete(SemesterDbHandler._table_name, idName, id)
        except Exception:
            return False

    @staticmethod
    def add(db: DbQuery, obj: Semester) -> bool:
        try:
            dictData = obj.toJson()
            return db.add(SemesterDbHandler._table_name, dictData)
        except Exception:
            return False

    @staticmethod
    def update(db: DbQuery, obj: Semester) -> bool:
        try:
            dictData = obj.toJson()
            return db.update(SemesterDbHandler._table_name, dictData, 'semesterID', obj.getSemesterID())
        except Exception:
            return False

    @staticmethod
    def toJson(array):
        data = {'semesterID': array[0],
                'semesterName': array[1],
                'gpa': array[2],
                'userID': array[3]
                }

        return data
    
    def updateGPA(db, semester: Semester):
        courses: list[CurrentCourse] = CourseDbHandler.get(db, 'semesterID', semester.semesterID, CourseDbHandler._tabel_name_current)

        if len(courses) == 0:
            semester.setGPA(4.0)
            SemesterDbHandler.update(db, semester)
            return
        
        total = 0
        for course in courses:
            CourseDbHandler.updateGrade(db, course)
            total += course.getGPAGrade()
        semester.setGPA(round(total/len(courses),2))
        SemesterDbHandler.update(db, semester)
