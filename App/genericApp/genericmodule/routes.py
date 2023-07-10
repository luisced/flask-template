from flask import Blueprint, jsonify
from genericApp.genericmodule.utils import *
from flask_restful import reqparse

user = Blueprint('user', __name__)


@user.route('/createUser', methods=['POST'])
def create_user_endpoint() -> dict[str:str]:
    '''Create a user and return a User object type'''

    # Request parsing
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument("name", type=str, location='json', required=True)
    parser.add_argument("username", type=str, location='json', required=True)
    parser.add_argument("email", type=str, location='json', required=True)
    parser.add_argument("password", type=str, location='json', required=True)
    parser.add_argument("birth_date", type=str, location='json', required=True)
    args = parser.parse_args(strict=True)
    data = None

    try:
        user = create_user(**args)
        print(user)
        if user:
            data = user
            message = 'User was successfully created'
            status_code = 200
            error = None
            code = 1
        else:
            message = 'Could not create user'
            status_code = 400
            error = 'User creation failed'
            code = 2

        return jsonify({
            'success': True,
            'message': message,
            'User': data,
            'status_code': status_code,
            'error': error,
            'code': code
        }), status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Could not create user',
            'status_code': 400,
            'error': str(e),
            'code': 2
        }), 400


@user.route('/getUser', methods=['GET'])
def get_user() -> dict[str:str]:
    '''Get user information'''

    # Request parsing
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument("id", type=int, location='args', required=True)
    args = parser.parse_args(strict=True)

    try:
        user = get_user(args['id'])
        if user:
            data = user.to_dict()
            message = f'User: {user.name}'
            status_code = 200
            error = None
            code = 1
        else:
            message = 'User not found'
            status_code = 404
            error = 'User not found'
            code = 2

        return jsonify({
            'success': True,
            'message': message,
            'User': data,
            'status_code': status_code,
            'error': error,
            'code': code
        }), status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Could not get user',
            'status_code': 400,
            'error': str(e),
            'code': 2
        }), 400


@user.route('/updateUser', methods=['PUT'])
def update_user() -> dict[str:str]:
    '''Update user information'''

    # Request parsing
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument("id", type=int, location='json', required=True)
    parser.add_argument("name", type=str, location='json', required=True)
    parser.add_argument("username", type=str, location='json', required=True)
    parser.add_argument("email", type=str, location='json', required=True)
    parser.add_argument("password", type=str, location='json', required=True)
    parser.add_argument("birth_date", type=str, location='json', required=True)
    args = parser.parse_args(strict=True)

    try:
        user = update_user(**args)
        if user:
            data = get_user(user.id).to_dict()
            message = 'User updated'
            status_code = 200
            error = None
            code = 1
        else:
            message = 'Could not update user'
            status_code = 400
            error = 'User update failed'
            code = 2

        return jsonify({
            'success': True,
            'message': message,
            'User': data,
            'status_code': status_code,
            'error': error,
            'code': code
        }), status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Could not update user',
            'status_code': 400,
            'error': str(e),
            'code': 2
        }), 400


@user.route('/deleteUser', methods=['DELETE'])
def delete_user() -> dict[str:str]:
    '''Delete user'''

    # Request parsing
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument("id", type=int, location='json', required=True)
    args = parser.parse_args(strict=True)

    try:
        user = delete_user(**args)
        if user:
            data = get_user(user.id).to_dict()
            message = f'User: {user.name}'
            status_code = 200
            error = None
            code = 1
        else:
            message = 'User not found'
            status_code = 404
            error = 'User not found'
            code = 2

        return jsonify({
            'success': True,
            'message': message,
            'User': data,
            'status_code': status_code,
            'error': error,
            'code': code
        }), status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Could not delete user',
            'status_code': 400,
            'error': str(e),
            'code': 2
        }), 400
