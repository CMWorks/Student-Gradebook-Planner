from obj.DbHandler import DbHandler
from database.dbQuery import DbQuery
from obj.Category import Category
from obj.AssignmnetDbHandler import AssignmnetDbHandler


class CategoryDbHandler(DbHandler):

    _tabel_name = 'CATEGORIES'

    @staticmethod
    def get(db: DbQuery, idName: str, id: str):
        new_objs: list[Category] = []
        try:
            data_list = db.get(CategoryDbHandler._tabel_name, idName, id)
            for obj in data_list:
                data = CategoryDbHandler.toJson(obj)
                new_objs.append(Category(data))
        except Exception:
            return []

        return new_objs

    @staticmethod
    def delete(db: DbQuery, idName: str, id) -> bool:
        try:
            return db.delete(CategoryDbHandler._tabel_name, idName, id)
        except Exception:
            return False

    @staticmethod
    def add(db: DbQuery, obj: Category) -> bool:
        try:
            dictData = obj.toJson()
            return db.add(CategoryDbHandler._tabel_name, dictData)
        except Exception:
            return False

    @staticmethod
    def update(db: DbQuery, obj: Category) -> bool:
        try:
            dictData = obj.toJson()
            return db.update(CategoryDbHandler._tabel_name, dictData, 'categoryID', obj.getCategoryID())
        except Exception:
            return False

    @staticmethod
    def toJson(array):
        data = {'categoryID': array[0],
                'categoryName': array[1],
                'weight': array[2],
                'categoryGrade': array[3],
                'courseID': array[4],
                'semesterID': array[5],
                'userID': array[6]
                }

        return data

    def updateCategoryGrade(db, category: Category):
        assignments = AssignmnetDbHandler.get(db, 'categoryID', category.categoryID)

        if len(assignments) == 0:
            category.setCategoryGrade(100)
            CategoryDbHandler.update(db, category)
            return

        total = 0
        num = 0
        for assignment in assignments:
            if assignment.isDone:
                total += assignment.getPercentGrade()
                num += 1
        
        if num == 0:
            category.setCategoryGrade(100)
        else:
            category.setCategoryGrade(total/num)
        CategoryDbHandler.update(db, category)