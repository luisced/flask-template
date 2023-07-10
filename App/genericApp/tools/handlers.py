class UserAlreadyExistsError(Exception):
    """Error raised when user already exists in DB"""

    def __init__(self, message=None):
        self.message: str = "User already exists in the database" if message is None else message
