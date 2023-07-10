from genericApp import db
from genericApp.models import User
from flask_bcrypt import generate_password_hash
from datetime import datetime
import logging


def create_user(name: str, username: str, email: str, password: str, birth_date: datetime) -> User:
    '''Create a user and return a User object type'''

    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(name=name, username=username, email=email,
                        password=generate_password_hash(password).decode('utf-8'), birth_date=birth_date)
            db.session.add(user)
            db.session.commit()
            return user.to_dict()
        else:
            raise ValueError(
                f'User with email: {email} already exists in the database'
            )
    except Exception as e:
        logging.error(e)
        raise


def get_user(id: int) -> dict[str:str]:
    '''Get user function in order to get user's info from DB'''

    try:
        user = User.query.filter_by(id=id).first()
        return user.to_dict()
    except Exception as e:
        logging.error(e)
        return None


def update_user(id: int, name: str, username: str, email: str, password: str, birth_date: datetime) -> User:
    '''Update user function in order to update user's info from DB'''

    try:
        user = User.query.filter_by(id=id).first()
        if user:
            user.name = name
            user.username = username
            user.email = email
            user.password = generate_password_hash(password).decode('utf-8')
            user.birth_date = birth_date
            db.session.commit()
            return user
        else:
            raise ValueError(
                f'User with id: {id} does not exist in the database'
            )

    except Exception as e:
        logging.error(e)
        return None


def delete_user(id: int) -> User:
    '''Delete user function in order to delete user's info from DB'''

    try:
        user = User.query.filter_by(id=id).first()
        if user:
            user.status = False
            db.session.commit()
            return user
        else:
            raise ValueError(
                f'User with id: {id} does not exist in the database'
            )

    except Exception as e:
        logging.error(e)
        return None
