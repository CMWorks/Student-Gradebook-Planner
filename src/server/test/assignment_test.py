from obj.Assignment import Assignment
from obj.AssignmentDbHandler import AssignmentDbHandler
from database.SQLQuery import SQLQuery
import pytest
from obj.CategoryDbHandler import CategoryDbHandler
from obj.CourseDbHandler import CourseDbHandler
from obj.SemesterDbHandler import SemesterDbHandler
from obj.UserDbHandler import UserDbHandler

# Command: python -m pytest -v
db = SQLQuery.getDbQuery("serverTest.txt")

#########################
# Helpful Functions
#########################

def id_setup():
    cleanup()
    category_dict = {'categoryID': 1000,
             'categoryName': 'Exams',
             'weight': 1,
             'categoryGrade': 98.1,
             'courseID': 100,
             'semesterID': 1,
             'userID': '12345'
             }
    
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
    db.add(CategoryDbHandler._table_name, category_dict)
    
def data():
    assign_data = {'assignmentID': 10000,
             'assignmentName': 'Exam1',
             'pointsReceived': 98,
             'totalPoints': 100,
             'percentGrade': 98.0,
             'dueDate': "2021-12-8",
             'isDone': 0,
             'categoryID': 1000,
             'courseID': 100,
             'semesterID': 1,
             'userID': '12345'
             }
    
    return assign_data
    
def setup() -> Assignment:
    cleanup()
    id_setup()
    
    dict = data()
    db.add(AssignmentDbHandler._table_name, dict)
    assign = Assignment(dict)
    return assign



def cleanup():
    db.delete(UserDbHandler._table_name, "userID", "12345")


#########################
# Inputing data correctly
#########################

def test_addAssignment_correctData_true():
    id_setup()
    assign_data = data()
    
    assignment = Assignment(assign_data)
    
    success = AssignmentDbHandler.add(db, assignment)
    new_assign = AssignmentDbHandler.get(db, "assignmentID", assignment.assignmentID)[0]
    
    cleanup()
    
    assert success and assignment.toJson() == new_assign.toJson()
    
def test_addAssignment_invalidData_KeyError():
    id_setup()
    
    with pytest.raises(KeyError) as exc_info:
        assignment = Assignment({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
    
def test_editAssignment_correctData_true():
    assignment = setup()
    
    assignment.setAssignmentName("__test__")
    
    success = AssignmentDbHandler.update(db, assignment)
    new_assign = AssignmentDbHandler.get(db, "assignmentID", assignment.assignmentID)[0]
    
    cleanup()
    
    assert success and assignment.toJson() == new_assign.toJson()
    
def test_editAssignment_invalidData_KeyError():
    with pytest.raises(KeyError) as exc_info:
        assignment = Assignment({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
def test_deleteAssignment_correctID_true():
    assignment = setup()
    
    success = AssignmentDbHandler.delete(db, "assignmentID", assignment.assignmentID)
    new_assign = AssignmentDbHandler.get(db, "assignmentID", assignment.assignmentID)
    
    cleanup()
    
    assert success and len(new_assign) == 0
    
def test_deleteAssignment_invalidID_false():
    assignment = setup()
    
    success = AssignmentDbHandler.delete(db, "assignmentID", 0)
    new_assign = AssignmentDbHandler.get(db, "assignmentID", assignment.assignmentID)
    
    cleanup()
    
    assert not success and len(new_assign) != 0

def test_markAssignment_correctData_true():
    assignment = setup()
    
    assignment.setIdDone(True)
    
    success = AssignmentDbHandler.update(db, assignment)
    new_assign = AssignmentDbHandler.get(db, "assignmentID", assignment.assignmentID)[0]
    
    cleanup()
    
    assert success and assignment.toJson() == new_assign.toJson()
    
def test_markAssignment_invalidData_KeyError():
    with pytest.raises(KeyError) as exc_info:
        assignment = Assignment({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    
    
def test_cleanup():
    cleanup()
    assert True
