from genericApp import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseModel(db.Model):
    '''Base Model to inherit from'''

    __abstract__ = True

    id: int = db.Column(db.Integer, primary_key=True)
    status: bool = db.Column(db.Boolean, nullable=False, default=True)
    creation_date: datetime = db.Column(
        db.Date, nullable=False, default=datetime.now)
    last_update: str = db.Column(
        db.TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now)

    def to_dict(self) -> dict:
        return {
            column.name: getattr(self, column.name).strftime(
                '%Y-%m-%d %H:%M:%S')
            if isinstance(getattr(self, column.name), datetime)
            else getattr(self, column.name)
            for column in self.__table__.columns
        }


@dataclass
class User(BaseModel):
    '''User model to interact with DB Table'''

    __tablename__ = 'User'

    name: str = db.Column(db.String(280), nullable=False)
    username: str = db.Column(db.String(280), nullable=False)
    email: str = db.Column(db.String(280), nullable=False)
    password: str = db.Column(db.String(280), nullable=False)
    birth_date: datetime = db.Column(
        db.Date, nullable=False)
