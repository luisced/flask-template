from flask import Blueprint
from genericApp.genericmodule.utils import *
from genericApp.tools.utils import parse_request, generate_response

user = Blueprint('user', __name__)


@user.route('/createUser', methods=['POST'])
def create_user_endpoint() -> dict[str:str]:
    args = parse_request("name", "username", "email", "password", "birth_date")

    try:
        user = create_user(**args)
        return generate_response(True, 'User was successfully created', user, 200)
    except Exception as e:
        return generate_response(False, 'Could not create user', None, 400, str(e))


@user.route('/getUser', methods=['GET'])
def get_user() -> dict[str:str]:
    '''Get user information'''
    args = parse_request("id", location='args')

    try:
        user = get_user(args['id'])
        return generate_response(True, f'User: {user.name}', user.to_dict(), 200)
    except Exception as e:
        return generate_response(False, 'Could not get user', None, 400, str(e))

@user.route('/updateUser', methods=['PUT'])
def update_user() -> dict[str:str]:
    '''Update user information'''
    args = parse_request("id", "name", "username", "email", "password", "birth_date")
    args['password'] = generate_password_hash(args['password'])

    try:
        user = update_user(**args)
        return generate_response(True, 'User updated', get_user(user.id).to_dict(), 200)
    except Exception as e:
        return generate_response(False, 'Could not update user', None, 400, str(e))

@user.route('/deleteUser', methods=['DELETE'])
def delete_user() -> dict[str:str]:
    '''Delete user'''
    args = parse_request("id")

    try:
        user = delete_user(**args)
        return generate_response(True, f'User: {user.name}', get_user(user.id).to_dict(), 200)
    except Exception as e:
        return generate_response(False, 'Could not delete user', None, 400, str(e))
