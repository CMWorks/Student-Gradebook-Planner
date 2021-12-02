from obj.Semester import Semester
from obj.SemesterDbHandler import SemesterDbHandler
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

def setup() -> Semester:
    cleanup()
    id_setup()
    
    sem_data = semester_data()
    db.add(SemesterDbHandler._table_name, sem_data)
    obj = Semester(sem_data)
    return obj


def cleanup():
    db.delete(UserDbHandler._table_name, "userID", "12345")


def semester_data():
    semesterData = {'semesterID': 1,
             'semesterName': 'Spring-2021',
             'gpa': 4.0,
             'userID': '12345',
             }
    return semesterData

#########################
# Inputing data correctly
#########################
def test_addSemester_correctData_true():

    id_setup()

    semester = Semester(semester_data())

    success = SemesterDbHandler.add(db, semester)
    new_semester = SemesterDbHandler.get(db, "semesterID", semester.semesterID)[0]

    cleanup()
    
    assert success and semester.toJson() == new_semester.toJson()
    
def test_addSemester_invalidData_KeyError():
    id_setup()
    
    with pytest.raises(KeyError) as exc_info:
        semester = Semester({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
    
def test_editSemester_correctData_true():
    semester = setup()
    
    semester.setSemesterName("__test__")
    
    success = SemesterDbHandler.update(db, semester)
    new_semester = SemesterDbHandler.get(db, "semesterID", semester.semesterID)[0]
    
    cleanup()
    
    assert success and semester.toJson() == new_semester.toJson()
    
def test_editSemester_invalidData_KeyError():
    with pytest.raises(KeyError) as exc_info:
        semester = Semester({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
def test_deleteSemester_correctID_true():
    semester = setup()
    
    success = SemesterDbHandler.delete(db, "semesterID", semester.semesterID)
    new_semester = SemesterDbHandler.get(db, "semesterID", semester.semesterID)
    
    cleanup()
    
    assert success and len(new_semester) == 0
    
def test_deleteSemester_invalidID_false():
    semester = setup()
    
    success = SemesterDbHandler.delete(db, "semesterID", 0)
    new_semester = SemesterDbHandler.get(db, "semesterID", semester.semesterID)
    
    cleanup()
    
    assert not success and len(new_semester) != 0


def test_cleanup():
    cleanup()
    assert True