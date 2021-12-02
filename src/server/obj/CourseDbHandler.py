from obj.DbHandler import DbHandler
from database.dbQuery import DbQuery
from obj.FutureCourse import FutureCourse
from obj.CurrentCourse import CurrentCourse
from obj.Category import Category
from obj.CategoryDbHandler import CategoryDbHandler
from obj.Course import Course


class CourseDbHandler(DbHandler):

    _table_name_future = 'FUTURE_COURSE'
    _table_name_current = 'CURRENT_COURSE'

    @staticmethod
    def get(db: DbQuery, idName: str, id: str, table: str):
        new_objs: list[Course] = []
        try:
            data_list = db.get(table, idName, id)
            for obj in data_list:
                data = CourseDbHandler.toJson(obj, table)
                if table == CourseDbHandler._table_name_current:
                    new_objs.append(CurrentCourse(data))
                else:
                    new_objs.append(FutureCourse(data))
        except Exception:
            return []

        return new_objs

    @staticmethod
    def delete(db: DbQuery, idName: str, id, table: str) -> bool:
        try:
            return db.delete(table, idName, id)
        except Exception:
            return False

    @staticmethod
    def add(db: DbQuery, obj: Course, table: str) -> bool:
        try:
            dictData = obj.toJson()
            return db.add(table, dictData)
        except Exception:
            return False

    @staticmethod
    def update(db: DbQuery, obj: Course, table: str) -> bool:
        try:
            dictData = obj.toJson()
            return db.update(table, dictData, 'courseID', obj.getCourseID())
        except Exception:
            return False

    @staticmethod
    def toJson(array, table: str):
        if table == CourseDbHandler._table_name_current:
            data = {'courseID': array[0],
                    'courseName': array[1],
                    'creditHours': array[2],
                    'isOnline': array[3],
                    'grade': array[4],
                    'semesterID': array[5],
                    'userID': array[6]
                    }
        else:
            data = {'courseID': array[0],
                    'courseName': array[1],
                    'creditHours': array[2],
                    'plannedSemester': array[3],
                    'userID': array[6]
                    }

        return data
    
    def updateGrade(db, course: CurrentCourse):
        categories: list[Category] = CategoryDbHandler.get(db, 'courseID', course.courseID)

        if len(categories) == 0:
            course.setGrade(100)
            CourseDbHandler.update(db, course, CourseDbHandler._table_name_current)
            return

        total = 0
        for category in categories:
            CategoryDbHandler.updateCategoryGrade(db, category)
            total += category.getCategoryGrade()*(category.getWeight()/100)
        course.setGrade(total)
        CourseDbHandler.update(db, course, CourseDbHandler._table_name_current)
