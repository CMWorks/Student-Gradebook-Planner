from obj.FutureCourse import FutureCourse
from obj.CourseDbHandler import CourseDbHandler
from database.SQLQuery import SQLQuery
import pytest
from obj.UserDbHandler import UserDbHandler

# Command: python -m pytest -v
db = SQLQuery.getDbQuery("serverTest.txt")

#########################
# Helpful Funcitons
#########################

def id_setup():
    cleanup()
    userData = {'userID': '12345',
             'firstName': 'Bob',
             'lastName': 'joe',
             'email': 'mail',
             'totalGPA': 4.3
             }
    
    db.add(UserDbHandler._table_name, userData)

def setup() -> FutureCourse:
    cleanup()
    id_setup()
    
    futureData = future_Futurecourse_data()
    db.add(CourseDbHandler._table_name_future, futureData)
    obj = FutureCourse(futureData)
    return obj


def cleanup():
    db.delete(UserDbHandler._table_name, "userID", "12345")


def future_Futurecourse_data():
    futureData = {'courseID': 10,
             'courseName': 'IT400',
             'creditHours': 3,
             'plannedSemester': 'FALL-2022',
             'userID': '12345',
             }
    return futureData

#########################
# Inputing data correctly
#########################
def test_addFutureCourse_correctData_true():

    id_setup()

    future_course = FutureCourse(future_Futurecourse_data())

    success = CourseDbHandler.add(db, future_course, CourseDbHandler._table_name_future)
    new_future_course = CourseDbHandler.get(db, "courseID", future_course.courseID, CourseDbHandler._table_name_future)[0]

    cleanup()
    
    assert success and future_course.toJson() == new_future_course.toJson()
    
def test_addFutureCourse_invalidData_KeyError():
    id_setup()
    
    with pytest.raises(KeyError) as exc_info:
        future_course = FutureCourse({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
    
def test_editFutureCourse_correctData_true():
    future_course = setup()
    
    future_course.setCourseName("__test__")
    
    success = CourseDbHandler.update(db, future_course, CourseDbHandler._table_name_future)
    new_future_course = CourseDbHandler.get(db, "courseID", future_course.courseID, CourseDbHandler._table_name_future)[0]
    
    cleanup()
    
    assert success and future_course.toJson() == new_future_course.toJson()
    
def test_editFutureCourse_invalidData_KeyError():
    with pytest.raises(KeyError) as exc_info:
        future_course = FutureCourse({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
def test_deleteFutureCourse_correctID_true():
    future_course = setup()
    
    success = CourseDbHandler.delete(db, "courseID", future_course.courseID, CourseDbHandler._table_name_future)
    new_future_course = CourseDbHandler.get(db, "courseID", future_course.courseID, CourseDbHandler._table_name_future)
    
    cleanup()
    
    assert success and len(new_future_course) == 0
    
def test_deleteFutureCourse_invalidID_false():
    future_course = setup()
    
    success = CourseDbHandler.delete(db, "courseID", 0, CourseDbHandler._table_name_future)
    new_future_course = CourseDbHandler.get(db, "courseID", future_course.courseID, CourseDbHandler._table_name_future)
    
    cleanup()
    
    assert not success and len(new_future_course) != 0


def test_cleanup():
    cleanup()
    assert True