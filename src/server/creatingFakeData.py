from database.SQLQuery import SQLQuery
from auth.jwtAuth import JWTAuth
from obj.User import User
from obj.Semester import Semester
from obj.CurrentCourse import CurrentCourse
from obj.FutureCourse import FutureCourse
from obj.Category import Category
from obj.Assignment import Assignment
from obj.Course import Course

db = SQLQuery.getDbQuery("serverTest.txt")

userData1 = {'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815',
             'firstName': 'Admin',
             'lastName': 'State',
             'email': 'admin@ilstu.edu',
             'totalGPA': 0
             }

semesterData2 = {'semesterID': 1,
                 'semesterName': 'Fall-2021',
                 'gpa': 4.0,
                 'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815',
                 }
semesterData1 = {'semesterID': 2,
                 'semesterName': 'Spring-2022',
                 'gpa': 3.8,
                 'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815',
                 }

futureData1 = {'courseID': 10,
               'courseName': 'IT400',
               'creditHours': 3,
               'plannedSemester': 'FALL-2022',
               'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815',
               }
futureData2 = {'courseID': 11,
               'courseName': 'IT388',
               'creditHours': 3,
               'plannedSemester': 'Spring-2023',
               'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815',
               }

currData1 = {'courseID': 110,
             'courseName': 'IT168',
             'creditHours': 3,
             'isOnline': 1,
             'grade': 98.2,
             'semesterID': 1,
             'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
             }
currData2 = {'courseID': 111,
             'courseName': 'IT179',
             'creditHours': 3,
             'isOnline': 1,
             'grade': 97.2,
             'semesterID': 1,
             'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
             }
currData3 = {'courseID': 112,
             'courseName': 'IT180',
             'creditHours': 3,
             'isOnline': 1,
             'grade': 96.2,
             'semesterID': 1,
             'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
             }
currData4 = {'courseID': 120,
             'courseName': 'IT326',
             'creditHours': 3,
             'isOnline': 0,
             'grade': 95.2,
             'semesterID': 2,
             'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
             }
currData5 = {'courseID': 121,
             'courseName': 'IT327',
             'creditHours': 3,
             'isOnline': 0,
             'grade': 94.2,
             'semesterID': 2,
             'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
             }
             
catData1 = {'categoryID': 1100,
            'categoryName': 'Exams',
            'weight': 1,
            'categoryGrade': 98.1,
            'courseID': 110,
            'semesterID': 1,
            'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
            }
catData2 = {'categoryID': 1110,
            'categoryName': 'Exams',
            'weight': 1,
            'categoryGrade': 97.1,
            'courseID': 111,
            'semesterID': 1,
            'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
            }
catData3 = {'categoryID': 1120,
            'categoryName': 'Exams',
            'weight': 1,
            'categoryGrade': 96.1,
            'courseID': 112,
            'semesterID': 1,
            'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
            }
catData4 = {'categoryID': 1200,
            'categoryName': 'Exams',
            'weight': 1,
            'categoryGrade': 95.1,
            'courseID': 120,
            'semesterID': 2,
            'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
            }
catData5 = {'categoryID': 1210,
            'categoryName': 'Exams',
            'weight': 1,
            'categoryGrade': 94.1,
            'courseID': 121,
            'semesterID': 2,
            'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
            }

assignData1 = {'assignmentID': 11000,
               'assignmentName': 'Exam1',
               'pointsReceived': 98,
               'totalPoints': 100,
               'percentGrade': 98.0,
               'dueDate': "2021-12-8",
               'isDone': 1,
               'categoryID': 1100,
               'courseID': 110,
               'semesterID': 1,
               'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
               }
assignData2 = {'assignmentID': 11100,
               'assignmentName': 'Exam1',
               'pointsReceived': 97,
               'totalPoints': 100,
               'percentGrade': 97.0,
               'dueDate': "2021-12-8",
               'isDone': 1,
               'categoryID': 1110,
               'courseID': 111,
               'semesterID': 1,
               'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
               }
assignData3 = {'assignmentID': 11200,
               'assignmentName': 'Exam1',
               'pointsReceived': 96,
               'totalPoints': 100,
               'percentGrade': 96.0,
               'dueDate': "2021-12-8",
               'isDone': 1,
               'categoryID': 1120,
               'courseID': 112,
               'semesterID': 1,
               'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
               }
assignData4 = {'assignmentID': 12000,
               'assignmentName': 'Exam1',
               'pointsReceived': 95,
               'totalPoints': 100,
               'percentGrade': 95.0,
               'dueDate': "2021-12-8",
               'isDone': 0,
               'categoryID': 1200,
               'courseID': 120,
               'semesterID': 2,
               'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
               }
assignData5 = {'assignmentID': 12100,
               'assignmentName': 'Exam2',
               'pointsReceived': 94,
               'totalPoints': 100,
               'percentGrade': 94.0,
               'dueDate': "2021-12-7",
               'isDone': 0,
               'categoryID': 1210,
               'courseID': 121,
               'semesterID': 2,
               'userID': '6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815'
               }

user = User(db, userData1)
print(user.addUser())
auth = JWTAuth(db)
print(auth.register('5211531068f4cb095735b32381fac242e63d80f1b7651c8fac727b1ec21c8f66','6a77b2f176b25fb407294fbcee0ef432e81eac03c32aa0409a10ca306f626815') is not False)
s1 = Semester(db, semesterData1)
print(s1.addSemester())
s2 = Semester(db, semesterData2)
print(s2.addSemester())
f1 = FutureCourse(db, futureData1)
print(f1.addCourse())
f2 = FutureCourse(db, futureData2)
print(f2.addCourse())
cur1 = CurrentCourse(db, currData1)
print(cur1.addCourse())
cur2 = CurrentCourse(db, currData2)
print(cur2.addCourse())
cur3 = CurrentCourse(db, currData3)
print(cur3.addCourse())
cur4 = CurrentCourse(db, currData4)
print(cur4.addCourse())
cur5 = CurrentCourse(db, currData5)
print(cur5.addCourse())
cat1 = Category(db, catData1)
print(cat1.addCategory())
cat2 = Category(db, catData2)
print(cat2.addCategory())
cat3 = Category(db, catData3)
print(cat3.addCategory())
cat4 = Category(db, catData4)
print(cat4.addCategory())
cat5 = Category(db, catData5)
print(cat5.addCategory())
as1 = Assignment(db, assignData1)
print(as1.addAssignment())
as2 = Assignment(db, assignData2)
print(as2.addAssignment())
as3 = Assignment(db, assignData3)
print(as3.addAssignment())
as4 = Assignment(db, assignData4)
print(as4.addAssignment())
as5 = Assignment(db, assignData5)
print(as5.addAssignment())