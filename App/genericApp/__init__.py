from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from genericApp.config import Config
import logging

# We create sqlalchemy instance
db = SQLAlchemy()

# Configure logging
logging.basicConfig(level=logging.INFO,)
formatter = logging.Formatter(
    '%(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# create app main function


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.config.from_object(Config)

    # We initiate ORM
    db.init_app(app)

    app.app_context().push()

    from genericApp.genericmodule.routes import user

    app.register_blueprint(user)

    return app
