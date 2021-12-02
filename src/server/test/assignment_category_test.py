from obj.Category import Category
from obj.CategoryDbHandler import CategoryDbHandler
from database.SQLQuery import SQLQuery
import pytest
from obj.CourseDbHandler import CourseDbHandler
from obj.SemesterDbHandler import SemesterDbHandler
from obj.UserDbHandler import UserDbHandler

# Command: python -m pytest -v
db = SQLQuery.getDbQuery("serverTest.txt")

#########################
# Helpful Funcitons
#########################

def id_setup():
    cleanup()
    currData = {'courseID': 100,
             'courseName': 'IT326',
             'creditHours': 3,
             'isOnline': 1,
             'grade': 98.2,
             'semesterID': 1,
             'userID': '12345'
             }
    
    semesterData = {'semesterID': 1,
             'semesterName': 'Spring-2021',
             'gpa': 4.0,
             'userID': '12345',
             }
    
    userData = {'userID': '12345',
             'firstName': 'Bob',
             'lastName': 'joe',
             'email': 'mail',
             'totalGPA': 4.3
             }
    
    db.add(UserDbHandler._table_name, userData)
    db.add(SemesterDbHandler._table_name, semesterData)
    db.add(CourseDbHandler._table_name_current, currData)

def setup() -> Category:
    cleanup()
    id_setup()
    
    category_dict = {'categoryID': 1000,
             'categoryName': 'Exams',
             'weight': 1,
             'categoryGrade': 98.1,
             'courseID': 100,
             'semesterID': 1,
             'userID': '12345'
             }
    db.add(CategoryDbHandler._table_name, category_dict)
    assign = Category(category_dict)
    return assign


def cleanup():
    db.delete(UserDbHandler._table_name, "userID", "12345")


def cat_data():
    category_dict = {'categoryID': 1000,
             'categoryName': 'Exams',
             'weight': 1,
             'categoryGrade': 98.1,
             'courseID': 100,
             'semesterID': 1,
             'userID': '12345'
             }
    return category_dict

#########################
# Inputing data correctly
#########################
def test_addCategory_correctData_true():
    id_setup()
    
    category = Category(cat_data())
    
    success = CategoryDbHandler.add(db, category)
    new_cat = CategoryDbHandler.get(db, "categoryID", category.categoryID)[0]
    
    cleanup()
    
    assert success and category.toJson() == new_cat.toJson()
    
def test_addCategory_invalidData_KeyError():
    id_setup()
    
    with pytest.raises(KeyError) as exc_info:
        category = Category({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
    
def test_editCategory_correctData_true():
    category = setup()
    
    category.setCategoryName("__test__")
    
    success = CategoryDbHandler.update(db, category)
    new_cat = CategoryDbHandler.get(db, "categoryID", category.categoryID)[0]
    
    cleanup()
    
    assert success and category.toJson() == new_cat.toJson()
    
def test_editCategory_invalidData_KeyError():
    with pytest.raises(KeyError) as exc_info:
        category = Category({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
def test_deleteCategory_correctID_true():
    category = setup()
    
    success = CategoryDbHandler.delete(db, "categoryID", category.categoryID)
    new_cat = CategoryDbHandler.get(db, "categoryID", category.categoryID)
    
    cleanup()
    
    assert success and len(new_cat) == 0
    
def test_deleteCategory_invalidID_false():
    category = setup()
    
    success = CategoryDbHandler.delete(db, "categoryID", 0)
    new_cat = CategoryDbHandler.get(db, "categoryID", category.categoryID)
    
    cleanup()
    
    assert not success and len(new_cat) != 0


def test_cleanup():
    cleanup()
    assert True