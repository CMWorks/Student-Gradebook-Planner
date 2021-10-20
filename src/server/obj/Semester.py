from database.dbQuery import DbQuery
from obj.CurrentCourse import CurrentCourse


class Semester:

    _tabel_name = 'Semester'

    def __init__(self, db: DbQuery, dictData: dict = None):
        if dictData is None:
            self.db = db
            self.semesterID = -1
            self.semesterName = ''
            self.gpa = 0.0
        else:
            self.db = db
            self.semesterID = dictData['semesterID']
            self.semesterName = dictData['semesterName']
            self.gpa = dictData['gpa']

    @staticmethod
    def getSemesters(db: DbQuery, idName, id):
        semData = db.get(Semester._tabel_name, idName, id)
        
        out:list[Semester] = []
        for data in semData:
            id = data[0]
            name = data[1]
            gpa = data[2]
            new_semester = Semester(db)
            new_semester.setSemesterID(id)
            new_semester.setSemesterName(name)
            new_semester.setGPA(gpa)
            out.append(new_semester)

        return out

    @staticmethod
    def deleteSemesters(db: DbQuery, idName, id):
        return db.delete(Semester._tabel_name, idName, id)

    def addSemester(self):
        listData = [self.getSemesterID(), self.getSemesterName(), self.getGPA()]
        return self.db.add(Semester._tabel_name, listData)

    def updateSemester(self):
        dictData = self.toJson()
        return self.db.update(Semester._tabel_name, dictData)

    def getSemesterID(self):
        return self.semesterID

    def getSemesterName(self):
        return self.semesterName

    def getGPA(self):
        return self.gpa

    def setSemesterID(self, id):
        self.semesterID = id

    def setSemesterName(self, name):
        self.semesterName = name

    def setGPA(self, gpa):
        self.gpa = gpa

    def toJson(self):
        data = {'semesterID':self.getSemesterID(),
                'semesterName': self.getSemesterName(),
                'gpa': self.getGPA()
                }
        return data

    def updateGPA(self):
        courses = CurrentCourse.getCourses(self.db, 'semesterID', self.semesterID)

        if len(courses) == 0:
            self.setGPA(0)
            return
        
        total = 0
        for course in courses:
            course.updateGrade()
            total += course.getGPAGrade()
        self.setGPA(total/len(courses))