from obj.CurrentCourse import CurrentCourse
from obj.CourseDbHandler import CourseDbHandler
from database.SQLQuery import SQLQuery
import pytest
from obj.SemesterDbHandler import SemesterDbHandler
from obj.UserDbHandler import UserDbHandler

# Command: python -m pytest -v
db = SQLQuery.getDbQuery("serverTest.txt")

#########################
# Helpful Funcitons
#########################

def id_setup():
    cleanup()
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

def setup() -> CurrentCourse:
    cleanup()
    id_setup()
    
    currData = {'courseID': 100,
             'courseName': 'IT326',
             'creditHours': 3,
             'isOnline': 1,
             'grade': 98.2,
             'semesterID': 1,
             'userID': '12345'
             }
    db.add(CourseDbHandler._table_name_current, currData)
    obj = CurrentCourse(currData)
    return obj


def cleanup():
    db.delete(UserDbHandler._table_name, "userID", "12345")


def course_data():
    currData = {'courseID': 100,
             'courseName': 'IT326',
             'creditHours': 3,
             'isOnline': 1,
             'grade': 98.2,
             'semesterID': 1,
             'userID': '12345'
             }
    return currData

#########################
# Inputing data correctly
#########################
def test_addCourse_correctData_true():

    id_setup()

    course = CurrentCourse(course_data())

    success = CourseDbHandler.add(db, course, CourseDbHandler._table_name_current)
    new_course = CourseDbHandler.get(db, "courseID", course.courseID, CourseDbHandler._table_name_current)[0]

    cleanup()
    
    assert success and course.toJson() == new_course.toJson()
    
def test_addCourse_invalidData_KeyError():
    id_setup()
    
    with pytest.raises(KeyError) as exc_info:
        course = CurrentCourse({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
    
def test_editCourse_correctData_true():
    course = setup()
    
    course.setCourseName("__test__")
    
    success = CourseDbHandler.update(db, course, CourseDbHandler._table_name_current)
    new_course = CourseDbHandler.get(db, "courseID", course.courseID, CourseDbHandler._table_name_current)[0]
    
    cleanup()
    
    assert success and course.toJson() == new_course.toJson()
    
def test_editCourse_invalidData_KeyError():
    with pytest.raises(KeyError) as exc_info:
        course = CurrentCourse({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
def test_deleteCourse_correctID_true():
    course = setup()
    
    success = CourseDbHandler.delete(db, "courseID", course.courseID, CourseDbHandler._table_name_current)
    new_course = CourseDbHandler.get(db, "courseID", course.courseID, CourseDbHandler._table_name_current)
    
    cleanup()
    
    assert success and len(new_course) == 0
    
def test_deleteCourse_invalidID_false():
    course = setup()
    
    success = CourseDbHandler.delete(db, "courseID", 0, CourseDbHandler._table_name_current)
    new_course = CourseDbHandler.get(db, "courseID", course.courseID, CourseDbHandler._table_name_current)
    
    cleanup()
    
    assert not success and len(new_course) != 0


def test_cleanup():
    cleanup()
    assert True