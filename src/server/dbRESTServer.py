from flask import Flask, request, jsonify
import json

from flask.wrappers import Response
from database.SQLQuery import SQLQuery
from auth.jwtAuth import JWTAuth
from obj.User import User
from obj.Semester import Semester
from obj.CurrentCourse import CurrentCourse
from obj.FutureCourse import FutureCourse
from obj.Category import Category
from obj.Assignment import Assignment
from obj.UserDbHandler import UserDbHandler
from obj.SemesterDbHandler import SemesterDbHandler
from obj.CourseDbHandler import CourseDbHandler
from obj.CategoryDbHandler import CategoryDbHandler
from obj.AssignmnetDbHandler import AssignmnetDbHandler

api = Flask(__name__)

white = ['http://localhost:3000', 'http://localhost:9000']


db = SQLQuery.getDbQuery("database/sqlData.txt")
# db = SQLQuery.getDbQuery("serverTest.txt")
auth = JWTAuth(db)


@api.after_request
def add_cors_headers(response: Response):
    if request.referrer is None:
        return response
    r = request.referrer[:-1]
    if r in white or True:
        response.headers.add('Access-Control-Allow-Origin', r)
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
        response.headers.add('X-UA-Compatible', 'IE=Edge,chrome=1')
        response.headers.add('Cache-Control', 'public, max-age=0')
        response.headers.add(
            'Access-Control-Allow-Headers', 'X-Requested-With')
        response.headers.add('Access-Control-Allow-Headers', 'Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, OPTIONS, PUT, DELETE')
    return response


def check_authorization():
    token = request.headers.get("authorization")
    if token is None or 'Bearer ' not in token:
        print("Not authorized to talk to database")
        return False
    success = auth.verify(token[7:])
    return success


def __calcualte(id):
    user = UserDbHandler.get(db, 'userID', id)
    if user is not None:
        UserDbHandler.updateGPA(db, user)


def calcualte_user(name, id):
    if name == None:
        __calcualte(id)
    elif name == Semester:
        sem = SemesterDbHandler.get(db, 'semesterID', id)
        if len(sem) == 1:
            __calcualte(sem[0].userID)
    elif name == CurrentCourse:
        course = CourseDbHandler.get(db, 'courseID', id, CourseDbHandler._tabel_name_current)
        if len(course) == 1:
            __calcualte(course[0].userID)
    elif name == Category:
        category = CategoryDbHandler.get(db, 'categoryID', id)
        if len(category) == 1:
            __calcualte(category[0].userID)
    elif name == Assignment:
        assign = AssignmnetDbHandler.get(db, 'assignmentID', id)
        if len(assign) == 1:
            __calcualte(assign[0].userID)


@api.route('/v1/auth/register', methods=['POST'])
def register_user():
    try:
        data = json.loads(request.data.decode('UTF-8'))
        user = User(data['user'])
    except Exception:
        return {'success': False, 'message': 'Incorrect Data'}, 404

    token = UserDbHandler.add(db, user)
    if token is False:
        print("Registeration Info Already Being Used")
        return {'success': False}, 401
    token = auth.register(data['eHash'], data['idHash'])
    if token is False:
        print("Registeration Info Already Being Used")
        return {'success': False}, 401
    else:
        print(f"New Token: {token}")
        return {'success': True, 'token': token}, 200


@api.route('/v1/auth/login', methods=['POST'])
def login_user():
    data = json.loads(request.data.decode('UTF-8'))
    token = auth.login(data['eHash'], data['idHash'])
    if token is False:
        print("Wrong Login Info")
        return {'success': False}, 401
    else:
        print(f" New Token: {token}")
        return {'success': True, 'token': token}, 200


@api.route('/v1/users/<id>', methods=['GET'])
def get_user(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    user: User = UserDbHandler.get(db, 'userID', id)
    if user is None:
        print("No user found")
        return {'success': False, 'message': 'Not Found'}, 404

    print('User found')
    return {'success': True, 'data': user.toJson()}, 200


@api.route('/v1/users', methods=['POST'])
def add_user():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    try:
        data = json.loads(request.data.decode('UTF-8'))
        user = User(data)
    except Exception:
        return {'success': False, 'message': 'Incorrect Data'}, 404

    success = UserDbHandler.add(db, user)
    if not success:
        print("unsuccessful to add user")
        return {'success': False, 'message': 'Not Found'}, 404

    print('successsfully added user')
    return {'success': True}, 200


@api.route('/v1/users/<id>', methods=['PUT'])
def update_user():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401

    try:
        data = json.loads(request.data.decode('UTF-8'))
        user = User(data)
    except Exception:
        return {'success': False, 'message': 'Incorrect Data'}, 404

    success = UserDbHandler.update(db, user)
    if not success:
        print("unsuccessful to update user")
        return {'success': False, 'message': 'Not Found'}, 404

    print('successsfully updated user')
    return {'success': True}, 200


@api.route('/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401

    success = UserDbHandler.delete(db, 'userID', id)
    if not success:
        print("unsuccessful to delete user")
        return {'success': False, 'message': 'Not Found'}, 404

    print('successsfully deleted user')
    return {'success': True}, 200


@api.route('/v1/semesters', methods=['GET'])
def get_all_semester():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    keyname = query[0]
    key = query[1]
    semesters = SemesterDbHandler.get(db, keyname, key)
    data = []
    for sem in semesters:
        data.append(sem.toJson())
    if len(data) == 0:
        return {'success': False, 'data': data}, 404
    else:
        return {'success': True, 'data': data}, 200


@api.route('/v1/semesters/<id>', methods=['GET'])
def get_semester(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    semester = SemesterDbHandler.get(db, 'semesterID', id)
    if len(semester) != 1:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True, 'data': semester[0].toJson()}, 200


@api.route('/v1/semesters', methods=['POST'])
def add_semester():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    sem = Semester(data)
    success = SemesterDbHandler.add(db, sem)
    calcualte_user(None, sem.userID)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['PUT'])
def update_semester(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    sem = Semester(data)
    success = SemesterDbHandler.update(db, sem)
    calcualte_user(None, sem.userID)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['DELETE'])
def delete_semester(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    calcualte_user(Semester, id)
    success = SemesterDbHandler.delete(db, 'semesterID', id)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/futureCourses', methods=['GET'])
def get_all_future_course():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    keyname = query[0]
    key = query[1]
    fCourse = CourseDbHandler.get(
        db, keyname, key, CourseDbHandler._tabel_name_future)
    data = []
    for course in fCourse:
        data.append(course.toJson())
    return {'success': True, 'data': data}, 200


@api.route('/v1/futureCourses/<id>', methods=['GET'])
def get_future_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    course = CourseDbHandler.get(
        db, 'courseID', id, CourseDbHandler._tabel_name_future)
    if len(course) != 1:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True, 'data': course[0].toJson()}, 200


@api.route('/v1/futureCourses', methods=['POST'])
def add_future_course():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    course = FutureCourse(data)
    success = CourseDbHandler.add(
        db, course, CourseDbHandler._tabel_name_future)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['PUT'])
def update_future_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    course = FutureCourse(data)
    success = CourseDbHandler.update(
        db, course, CourseDbHandler._tabel_name_future)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['DELETE'])
def delete_future_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    success = CourseDbHandler.delete(
        db, 'courseID', id, CourseDbHandler._tabel_name_future)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/currentCourses', methods=['GET'])
def get_all_current_course():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    keyname = query[0]
    key = query[1]
    cCourse = CourseDbHandler.get(
        db, keyname, key, CourseDbHandler._tabel_name_current)
    data = []
    for course in cCourse:
        data.append(course.toJson())
    return {'success': True, 'data': data}, 200


@api.route('/v1/currentCourses/<id>', methods=['GET'])
def get_current_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    course = CourseDbHandler.get(
        db, 'courseID', id, CourseDbHandler._tabel_name_current)
    if len(course) != 1:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True, 'data': course[0].toJson()}, 200


@api.route('/v1/currentCourses', methods=['POST'])
def add_current_course():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    course = CurrentCourse(data)
    success = CourseDbHandler.add(
        db, course, CourseDbHandler._tabel_name_current)
    calcualte_user(None, course.userID)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['PUT'])
def update_current_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    course = CurrentCourse(data)
    success = CourseDbHandler.update(
        db, course, CourseDbHandler._tabel_name_current)
    calcualte_user(None, course.userID)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['DELETE'])
def delete_current_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    calcualte_user(CurrentCourse, id)
    success = CourseDbHandler.delete(
        db, 'courseID', id, CourseDbHandler._tabel_name_current)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/categories', methods=['GET'])
def get_all_category():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    keyname = query[0]
    key = query[1]
    category = CategoryDbHandler.get(db, keyname, key)
    data = []
    for cat in category:
        data.append(cat.toJson())
    return {'success': True, 'data': data}, 200


@api.route('/v1/categories/<id>', methods=['GET'])
def get_category(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    category = CategoryDbHandler.get(db, 'categoryID', id)
    if len(category) != 1:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True, 'data': category[0].toJson()}, 200


@api.route('/v1/categories', methods=['POST'])
def add_category():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    category = Category(data)
    success = CategoryDbHandler.add(db, category)
    calcualte_user(None, category.userID)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['PUT'])
def update_category(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    category = Category(data)
    success = CategoryDbHandler.update(db, category)
    calcualte_user(None, category.userID)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['DELETE'])
def delete_category(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    calcualte_user(Category, id)
    success = CategoryDbHandler.delete(db, 'categoryID', id)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/assignments', methods=['GET'])
def get_all_assignment():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    keyname = query[0]
    key = query[1]
    assignment = AssignmnetDbHandler.get(db, keyname, key)
    data = []
    for ment in assignment:
        data.append(ment.toJson())
    return {'success': True, 'data': data}, 200


@api.route('/v1/assignments/<id>', methods=['GET'])
def get_assignment(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    assignment = AssignmnetDbHandler.get(db, 'assignmentID', id)
    if len(assignment) != 1:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True, 'data': assignment[0].toJson()}, 200


@api.route('/v1/assignments', methods=['POST'])
def add_assignment():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    assignment = Assignment(data)
    success = AssignmnetDbHandler.add(db, assignment)
    calcualte_user(None, assignment.userID)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['PUT'])
def update_assignment(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    assignment = Assignment(data)
    success = AssignmnetDbHandler.update(db, assignment)
    calcualte_user(None, assignment.userID)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['DELETE'])
def delete_assignment(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    calcualte_user(Assignment, id)
    success = AssignmnetDbHandler.delete(db, 'assignmentID', id)
    if not success:
        return {'success': False, 'message': 'Not Found'}, 404

    return {'success': True}, 200


if __name__ == '__main__':
    api.run()
