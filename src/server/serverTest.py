from database.SQLQuery import SQLQuery
from auth.jwtAuth import JWTAuth
from obj.User import User
from obj.Semester import Semester
from obj.CurrentCourse import CurrentCourse
from obj.FutureCourse import FutureCourse
from obj.Category import Category
from obj.Assignment import Assignment
from obj.Course import Course

db = SQLQuery.getDbQuery("database/sqlData.txt")

print("""-----USER-----""")
userData1 = {'userID': '12345',
             'firstName': 'Bob',
             'lastName': 'joe',
             'email': 'mail',
             'totalGPA': 4.3
             }
updatedUser1 = {'userID': '12345',
             'firstName': 'Bob',
             'lastName': 'joe',
             'email': 'bird',
             'totalGPA': 4.3
             }
u1 = User(db, userData1)
u2 = User(db, updatedUser1)
# Testing adding user
print(True,u1.addUser())
# testing adding same user
print(False,u1.addUser())
# testing getting user
print(userData1 == User.getUser(db, '12345').toJson())
# testing updating user
print(True,u2.updateUser())
# testing getting updated user
print(updatedUser1 == User.getUser(db, '12345').toJson())
# testing deleting user
print(True,User.deleteUser(db, '12345'))
# testing deleting user
print(False,User.deleteUser(db, '12345'))
# testing getting user
print(None,User.getUser(db, '12345'))

print('\n',"""-----SEMESTER-----""")
u1.addUser()
semesterData1 = {'semesterID': 1,
             'semesterName': 'Spring-2021',
             'gpa': 4.0,
             'userID': '12345',
             }
updatedSemester1 = {'semesterID': 1,
             'semesterName': 'Fall-2021',
             'gpa': 4.0,
             'userID': '12345',
             }
s1 = Semester(db, semesterData1)
s2 = Semester(db, updatedSemester1)
# Testing adding semester
print(True,s1.addSemester())
# testing adding same semester
print(False,s1.addSemester())
# testing getting semester
print(semesterData1 == Semester.getSemesters(db, 'semesterID', 1)[0].toJson())
# testing updating semester
print(True,s2.updateSemester())
# testing getting updated semester
print(updatedSemester1 == Semester.getSemesters(db,  'semesterID', 1)[0].toJson())
# testing deleting semester
print(True,Semester.deleteSemesters(db, 'semesterID', 1))
# testing deleting semester
print(False,Semester.deleteSemesters(db, 'semesterID', 1))
# testing getting semester
print([],Semester.getSemesters(db, 'semesterID', 1))
User.deleteUser(db, '12345')

print('\n',"""-----FUTURE_COURSE-----""")
u1.addUser()
s1.addSemester()
futureData1 = {'courseID': 10,
             'courseName': 'IT400',
             'creditHours': 3,
             'plannedSemester': 'FALL-2022',
             'userID': '12345',
             }
updatedFuture1 = {'courseID': 10,
             'courseName': 'IT420',
             'creditHours': 3,
             'plannedSemester': 'FALL-2022',
             'userID': '12345',
             }
f1 = FutureCourse(db, futureData1)
f2 = FutureCourse(db, updatedFuture1)
# Testing adding semester
print(True,f1.addCourse())
# testing adding same semester
print(False,f1.addCourse())
# testing getting semester
print(futureData1 == FutureCourse.getCourses(db, 'courseID', 10)[0].toJson())
# testing updating semester
print(True,f2.updateCourse())
# testing getting updated semester
print(updatedFuture1 == FutureCourse.getCourses(db,  'courseID', 10)[0].toJson())
# testing deleting semester
print(True,FutureCourse.deleteCourses(db, 'courseID', 10))
# testing deleting semester
print(False,FutureCourse.deleteCourses(db, 'courseID', 10))
# testing getting semester
print([],FutureCourse.getCourses(db, 'courseID', 10))

print('\n',"""-----Current_COURSE-----""")
u1.addUser()
s1.addSemester()
f1.addCourse()
currData1 = {'courseID': 100,
             'courseName': 'IT326',
             'creditHours': 3,
             'isOnline': 1,
             'grade': 98.2,
             'semesterID': 1,
             'userID': '12345'
             }
updatedCurr1 = {'courseID': 100,
             'courseName': 'IT326',
             'creditHours': 3,
             'isOnline': 0,
             'grade': 98.2,
             'semesterID': 1,
             'userID': '12345',
             }
co1 = CurrentCourse(db, currData1)
co2 = CurrentCourse(db, updatedCurr1)
# Testing adding semester
print(True,co1.addCourse())
# testing adding same semester
print(False,co1.addCourse())
# testing getting semester
print(currData1 == CurrentCourse.getCourses(db, 'courseID', 100)[0].toJson())
# testing updating semester
print(True,co2.updateCourse())
# testing getting updated semester
print(updatedCurr1 == CurrentCourse.getCourses(db,  'courseID', 100)[0].toJson())
# testing deleting semester
print(True,CurrentCourse.deleteCourses(db, 'courseID', 100))
# testing deleting semester
print(False,CurrentCourse.deleteCourses(db, 'courseID', 100))
# testing getting semester
print([],CurrentCourse.getCourses(db, 'courseID', 100))

print('\n',"""-----CATEGORY-----""")
u1.addUser()
s1.addSemester()
f1.addCourse()
co1.addCourse()
catData1 = {'categoryID': 1000,
             'categoryName': 'Exams',
             'weight': 1,
             'categoryGrade': 98.1,
             'courseID': 100,
             'semesterID': 1,
             'userID': '12345'
             }
updatedCat1 = {'categoryID': 1000,
             'categoryName': 'Tests',
             'weight': 1,
             'categoryGrade': 98.1,
             'courseID': 100,
             'semesterID': 1,
             'userID': '12345'
             }
ca1 = Category(db, catData1)
ca2 = Category(db, updatedCat1)
# Testing adding semester
print(True,ca1.addCategory())
# testing adding same semester
print(False,ca1.addCategory())
# testing getting semester
print(catData1 == Category.getCategories(db, 'categoryID', 1000)[0].toJson())
# testing updating semester
print(True,ca2.updateCategory())
# testing getting updated semester
print(updatedCat1 == Category.getCategories(db,  'categoryID', 1000)[0].toJson())
# testing deleting semester
print(True,Category.deleteCategories(db, 'categoryID', 1000))
# testing deleting semester
print(False,Category.deleteCategories(db, 'categoryID', 1000))
# testing getting semester
print([],Category.getCategories(db, 'categoryID', 1000))

print('\n',"""-----ASSIGNMENT-----""")
u1.addUser()
s1.addSemester()
f1.addCourse()
co1.addCourse()
ca1.addCategory()
assignData1 = {'assignmentID': 10000,
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
updatedAssign1 = {'assignmentID': 10000,
             'assignmentName': 'Test1',
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
a1 = Assignment(db, assignData1)
a2 = Assignment(db, updatedAssign1)
# Testing adding semester
print(True,a1.addAssignment())
# testing adding same semester
print(False,a1.addAssignment())
# testing getting semester
print(assignData1 == Assignment.getAssignments(db, 'assignmentID', 10000)[0].toJson())
# testing updating semester
print(True,a2.updateAssignment())
# testing getting updated semester
print(updatedAssign1 == Assignment.getAssignments(db,  'assignmentID', 10000)[0].toJson())
# testing deleting semester
print(True,Assignment.deleteAssignments(db, 'assignmentID', 10000))
# testing deleting semester
print(False,Assignment.deleteAssignments(db, 'assignmentID', 10000))
# testing getting semester
print([],Assignment.getAssignments(db, 'assignmentID', 10000))


print('\n',"""-----CASCADIG-----""")
u1.addUser()
s1.addSemester()
f1.addCourse()
co1.addCourse()
ca1.addCategory()
a1.addAssignment()
User.deleteUser(db, '12345')
print([] == Assignment.getAssignments(db, 'assignmentID', 10000))
s1.addSemester()
co1.addCourse()
ca1.addCategory()
a1.addAssignment()
Semester.deleteSemesters(db, 'semesterID', 1)
print([] == Assignment.getAssignments(db, 'assignmentID', 10000))
co1.addCourse()
ca1.addCategory()
a1.addAssignment()
CurrentCourse.deleteCourses(db, 'courseID', 100)
print([] == Assignment.getAssignments(db, 'assignmentID', 10000))
ca1.addCategory()
a1.addAssignment()
Category.deleteCategories(db, 'categoryID', 1000)
print([] == Assignment.getAssignments(db, 'assignmentID', 10000))