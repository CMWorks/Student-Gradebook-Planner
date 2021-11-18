from obj.DbHandler import DbHandler
from database.dbQuery import DbQuery
from obj.Assignment import Assignment


class AssignmnetDbHandler(DbHandler):

    _tabel_name = 'ASSIGNMENTS'

    @staticmethod
    def get(db: DbQuery, idName: str, id: str):
        new_objs: list[Assignment] = []
        try:
            data_list = db.get(AssignmnetDbHandler._tabel_name, idName, id)
            for obj in data_list:
                data = AssignmnetDbHandler.toJson(obj)
                new_objs.append(Assignment(data))
        except Exception as e:
            print(e)
            return []

        return new_objs

    @staticmethod
    def delete(db: DbQuery, idName: str, id) -> bool:
        try:
            return db.delete(AssignmnetDbHandler._tabel_name, idName, id)
        except Exception:
            return False

    @staticmethod
    def add(db: DbQuery, obj: Assignment) -> bool:
        try:
            dictData = obj.toJson()
            return db.add(AssignmnetDbHandler._tabel_name, dictData)
        except Exception:
            return False

    @staticmethod
    def update(db: DbQuery, obj: Assignment) -> bool:
        obj.calculateGrade()
        try:
            dictData = obj.toJson()
            return db.update(AssignmnetDbHandler._tabel_name, dictData, 'assignmentID', obj.getAssignmentID())
        except Exception:
            return False

    @staticmethod
    def toJson(array):
        data = {'assignmentID': array[0],
                'assignmentName': array[1],
                'pointsReceived': array[2],
                'totalPoints': array[3],
                'percentGrade': array[4],
                'dueDate': array[5],
                'isDone': array[6],
                'categoryID': array[7],
                'courseID': array[8],
                'semesterID': array[9],
                'userID': array[10]
                }

        return data
