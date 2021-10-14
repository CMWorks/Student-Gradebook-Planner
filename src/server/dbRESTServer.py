from flask import Flask, request, jsonify
import json
from database.SQLQuery import SQLQuery
from auth.jwtAuth import JWTAuth

api = Flask(__name__)

white = ['http://localhost:3000', 'http://localhost:9000']


db = SQLQuery("database/sqlData.txt")
auth = JWTAuth(db)


@api.after_request
def add_cors_headers(response):
    if request.referrer is None:
        return response
    r = request.referrer[:-1]
    if r in white or True:
        response.headers.add('Access-Control-Allow-Origin', r)
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
        response.headers.add(
            'Access-Control-Allow-Headers', 'X-Requested-With')
        response.headers.add('Access-Control-Allow-Headers', 'Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, OPTIONS, PUT, DELETE')
    return response


def check_authorization():
    token = request.headers.get("authorization")
    if token is None or 'Bearer ' not in token:
        return False
    success = auth.verify(token[7:])
    return success


@api.route('/v1/auth/register', methods=['POST'])
def register_user():
    data = json.loads(request.data.decode('UTF-8'))
    token = auth.register(data['eHash'], data['iHash'])
    if token is False:
        return {'success': False}, 401
    else:
        print(f"\033[34mNew Token: {token}\033[0m")
        return {'success': True, 'token': token}, 200


@api.route('/v1/auth/login', methods=['POST'])
def login_user():
    data = json.loads(request.data.decode('UTF-8'))
    token = auth.login(data['eHash'], data['iHash'])
    if token is False:
        return {'success': False}, 401
    else:
        print(f"\033[34m New Token: {token}\033[0m")
        return {'success': True, 'token': token}, 200


@api.route('/v1/users/<id>', methods=['GET'])
def get_user(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/users/<id>', methods=['POST'])
def add_user(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/users/<id>', methods=['PUT'])
def update_user(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/semesters', methods=['GET'])
def get_all_semester():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    foreign_key = query[1]
    return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['GET'])
def get_semester(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['POST'])
def add_semester(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['PUT'])
def update_semester(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['DELETE'])
def delete_semester(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/futureCourses', methods=['GET'])
def get_all_future_course():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    foreign_key = query[1]
    return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['GET'])
def get_future_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['POST'])
def add_future_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['PUT'])
def update_future_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['DELETE'])
def delete_future_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/currentCourses', methods=['GET'])
def get_all_current_course():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    foreign_key = query[1]
    return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['GET'])
def get_current_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['POST'])
def add_current_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['PUT'])
def update_current_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['DELETE'])
def delete_current_course(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/categories', methods=['GET'])
def get_all_category():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    foreign_key = query[1]
    return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['GET'])
def get_category(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['POST'])
def add_category(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['PUT'])
def update_category(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['DELETE'])
def delete_category(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/assignments', methods=['GET'])
def get_all_assignment():
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    query = request.query_string.decode('UTF-8').split('=')
    if len(query) is not 2:
        return {'success': False}, 403
    foreign_key = query[1]
    return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['GET'])
def get_assignment(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['POST'])
def add_assignment(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['PUT'])
def update_assignment(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    data = json.loads(request.data.decode('UTF-8'))
    return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['DELETE'])
def delete_assignment(id):
    authorized = check_authorization()
    if not authorized:
        return {'success': False, 'message': 'Unauthorized'}, 401
    return {'success': True}, 200


if __name__ == '__main__':
    api.run()
