from database.dbQuery import DbQuery
from obj.Assignment import Assignment


class Category:

    _tabel_name = 'Category'

    def __init__(self, db: DbQuery, dictData: dict = None):
        if dictData is None:
            self.db = db
            self.categoryID = -1
            self.categoryName = ""
            self.weight = 1
            self.categoryGrade = 0.0
        else:
            self.db = db
            self.categoryID = dictData['categoryID']
            self.categoryName = dictData['categoryName']
            self.weight = dictData['weight']
            self.categoryGrade = dictData['categoryGrade']

    @staticmethod
    def getCategories(db: DbQuery, idName, id):
        categoryData = db.get(Category._tabel_name, idName, id)
        
        out:list[Category] = []
        for data in categoryData:
            id = data[0]
            name = data[1]
            weight = data[2]
            grade = data[3]
            new_category = Category(db)
            new_category.setCategoryID(id)
            new_category.setCategoryName(name)
            new_category.setWeight(weight)
            new_category.setCategoryGrade(grade)
            out.append(new_category)

        return out

    @staticmethod
    def deleteCategories(db: DbQuery, idName, id):
        return db.delete(Category._tabel_name, idName, id)

    def addCategory(self):
        listData = [self.getCategoryID(), self.getCategoryName(), self.getWeight(), self.getCategoryGrade()]
        return self.db.add(Category._tabel_name, listData)

    def updateCategory(self):
        dictData = self.toJson()
        return self.db.update(Category._tabel_name, dictData)

    def getCategoryName(self):
        return self.categoryGrade

    def getWeight(self):
        return self.weight

    def getCategoryGrade(self):
        return self.categoryGrade

    def getCategoryID(self):
        return self.categoryID

    def setCategoryID(self, id):
        self.categoryID = id

    def setCategoryName(self, name):
        self.categoryName = name

    def setWeight(self, weight):
        self.weight = weight

    def setCategoryGrade(self, grade):
        self.categoryGrade = grade

    def toJson(self):
        data = {'categoryID':self.getCategoryID(),
                'categoryName': self.getCategoryName(),
                'weight': self.getWeight(),
                'categoryGrade': self.getCategoryGrade()
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