from flask import Flask, request, jsonify
import json
from obj.User import User

api = Flask(__name__)

white = ['http://localhost:3000', 'http://localhost:9000']

User.addFutureCourse()

@api.after_request
def add_cors_headers(response):
	if request.referrer is None:
		return response
	r = request.referrer[:-1]
	if r in white:
		response.headers.add('Access-Control-Allow-Origin', r)
		response.headers.add('Access-Control-Allow-Credentials', 'true')
		response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
		response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
		response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
		response.headers.add('Access-Control-Allow-Headers', 'Authorization')
		response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
	return response


@api.route('/v1/users/<id>', methods=['GET'])
def get_user(id):
	return {'success': True}, 200


@api.route('/v1/users/<id>', methods=['POST'])
def add_user(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/users/<id>', methods=['PUT'])
def update_user(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
	return {'success': True}, 200


@api.route('/v1/semesters', methods=['GET'])
def get_all_semester():
	query = request.query_string.decode('UTF-8').split('=')
	if len(query) is not 2:
		return {'success': False}, 403
	foreign_key = query[1]
	return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['GET'])
def get_semester(id):
	return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['POST'])
def add_semester(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['PUT'])
def update_semester(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/semesters/<id>', methods=['DELETE'])
def delete_semester(id):
	return {'success': True}, 200


@api.route('/v1/futureCourses', methods=['GET'])
def get_all_future_course():
	query = request.query_string.decode('UTF-8').split('=')
	if len(query) is not 2:
		return {'success': False}, 403
	foreign_key = query[1]
	return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['GET'])
def get_future_course(id):
	return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['POST'])
def add_future_course(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['PUT'])
def update_future_course(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/futureCourses/<id>', methods=['DELETE'])
def delete_future_course(id):
	return {'success': True}, 200


@api.route('/v1/currentCourses', methods=['GET'])
def get_all_current_course():
	query = request.query_string.decode('UTF-8').split('=')
	if len(query) is not 2:
		return {'success': False}, 403
	foreign_key = query[1]
	return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['GET'])
def get_current_course(id):
	return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['POST'])
def add_current_course(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['PUT'])
def update_current_course(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/currentCourses/<id>', methods=['DELETE'])
def delete_current_course(id):
	return {'success': True}, 200


@api.route('/v1/categories', methods=['GET'])
def get_all_category():
	query = request.query_string.decode('UTF-8').split('=')
	if len(query) is not 2:
		return {'success': False}, 403
	foreign_key = query[1]
	return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['GET'])
def get_category(id):
	return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['POST'])
def add_category(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['PUT'])
def update_category(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/categories/<id>', methods=['DELETE'])
def delete_category(id):
	return {'success': True}, 200


@api.route('/v1/assignments', methods=['GET'])
def get_all_assignment():
	query = request.query_string.decode('UTF-8').split('=')
	if len(query) is not 2:
		return {'success': False}, 403
	foreign_key = query[1]
	return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['GET'])
def get_assignment(id):
	return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['POST'])
def add_assignment(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['PUT'])
def update_assignment(id):
	data = json.loads(request.data.decode('UTF-8'))
	return {'success': True}, 200


@api.route('/v1/assignments/<id>', methods=['DELETE'])
def delete_assignment(id):
	return {'success': True}, 200


if __name__ == '__main__':
	api.run()
