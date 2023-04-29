from flask import Blueprint, request, jsonify
from genericApp.genericmodule.utils import *

user = Blueprint('user', __name__)


@user.route('/create_user', methods=['POST'])
def create_user_route():
    '''Create a user and return a User object type'''

    json_data = request.get_json()
    data: list[dict[str, str]] = []
    response: dict[str, str] = {}
    error, code = None, None
    required_fields = ['name', 'username', 'email', 'password', 'birth_date']
    if request.method == 'POST':
        if not json_data:
            error = 'No input data provided'
            code = 400
        elif not all(fields in json_data for fields in required_fields):
            logging.info(json_data)
            error = f'Missing key: {", ".join(fields for fields in required_fields if fields not in json_data)}'
            logging.error("missing key")
            code = 400
        else:
            user = create_user(**json_data)
            if user:
                logging.info("User Created")
                data = user.to_dict()
                message = 'User was succesfully created'
                code = 200

    else:
        error = 'Method not allowed'
        code = 405

    response.update({'sucess': True, 'message': message, 'User': data, 'status_code': 200, 'error': error, 'code': code} if data and data != [] and data != [None] else {
        'sucess': False,  'message': 'Could not get content', 'status_code': 400, 'error': f'{error}', 'code': code})
    return jsonify(response)


@user.route('/get_user', methods=['GET'])
def get_user_route():
    json_data = request.get_json()
    data: list[dict[str, str]] = []
    response: dict[str, str] = {}
    error, code = None, None

    if request.method == 'GET':
        if not json_data:
            error = 'No input data provided'
            code = 400
        else:
            data = get_user(**json_data)
            if data:
                logging.info("Succesfully get user data")
                message = f'user: {user.name}'
                code = 200
            else:
                logging.info("User not found")
                message = f'User not found'
                code = 404
    else:
        error = 'Method not allowed'
        code = 405

    response.update({'sucess': True, 'message': message, 'User': data, 'status_code': 200, 'error': error, 'code': code} if data and data != [] and data != [None] else {
        'sucess': False,  'message': 'Could not get content', 'status_code': 400, 'error': f'{error}', 'code': code})
    return jsonify(response)


@user.route('/update_user', methods=['PUT'])
def update_user_route():
    json_data = request.get_json()
    data: list[dict[str, str]] = []
    response: dict[str, str] = {}
    error, code = None, None
    required_fields = ['id', 'name', 'username',
                       'email', 'password', 'birth_date']

    if request.method == 'PUT':
        if not json_data:
            error = 'No input data provided'
            code = 400
        elif not all(fields in json_data for fields in required_fields):
            logging.info(json_data)
            error = f'Missing key: {", ".join(fields for fields in required_fields if fields not in json_data)}'
            logging.error("missing key")
            code = 400
        else:
            user = update_user(**json_data)
            if user:
                logging.info("User updated")
                data = get_user(user.id)
                message = 'User was succesfully created'
                code = 200
    else:
        error = 'Method not allowed'
        code = 405

    response.update({'sucess': True, 'message': message, 'User': data, 'status_code': 200, 'error': error, 'code': code} if data and data != [] and data != [None] else {
        'sucess': False,  'message': 'Could not get content', 'status_code': 400, 'error': f'{error}', 'code': code})
    return jsonify(response)


@user.route('/delete_user', methods=['DELETE'])
def delete_user_route():
    json_data = request.get_json()
    data: list[dict[str, str]] = []
    response: dict[str, str] = {}
    error, code = None, None

    if request.method == 'DELETE':
        if not json_data:
            error = 'No input data provided'
            code = 400
        else:
            user = delete_user(**json_data)
            if user:
                logging.info("User deleted")
                data = get_user(user.id)
                message = f'user: {user.name}'
                code = 200
            else:
                logging.info("User not found")
                message = f'User not found'
                code = 404
    else:
        error = 'Method not allowed'
        code = 405

    response.update({'sucess': True, 'message': message, 'User': data, 'status_code': 200, 'error': error, 'code': code} if data and data != [] and data != [None] else {
        'sucess': False,  'message': 'Could not get content', 'status_code': 400, 'error': f'{error}', 'code': code})
    return jsonify(response)
