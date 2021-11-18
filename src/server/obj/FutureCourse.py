from obj.Course import Course


class FutureCourse(Course):

    def __init__(self, dictData: dict = None):
        super().__init__(dictData)
        if dictData is None:
            self.plannedSemester = ""
        else:
            self.plannedSemester = dictData['plannedSemester']

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