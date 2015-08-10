from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
import os

####                ####
####     config     ####
####	            ####

app = Flask(__name__)
# from_object() searches for UPPERCASE objects
app.config.from_object(os.environ['APP_SETTINGS'])
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
db = SQLAlchemy(app)

from project.main.views import main_blueprint

# The view that handles the authentication
login_manager.login_view = "main.login"


# register the blueprint
app.register_blueprint(main_blueprint)

from .models import Users


# Store session for the user via model ID
@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter(Users.id == int(user_id)).first()
