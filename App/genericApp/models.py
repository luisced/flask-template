from genericApp import db
from datetime import datetime

class BaseModel(db.Model):
    """
    An abstract base model class that defines some common attributes for all models in the application.
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False, default=True)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """
        Returns a dictionary representation of the model.
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }


class User(BaseModel):
    """
    A model class that represents a user in the application.
    """
    __tablename__ = 'User'
    name = db.Column(db.String(280), nullable=False)
    username = db.Column(db.String(280), nullable=False)
    email = db.Column(db.String(280), nullable=False)
    password = db.Column(db.String(280), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)