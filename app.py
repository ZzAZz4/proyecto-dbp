from model.entities import *
from database import connector
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import login_required, current_user, login_user, logout_user
from flask_login import LoginManager
from flask_login import current_user

from flask_wtf import CSRFProtect


db = connector.Manager()
engine = db.create_engine()
csrf = CSRFProtect()

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')


csrf.init_app(app)
migrate = Migrate(app, db)

user_manager = UserManager(app, db, Usuario)


# User Create
def create_user():
    pass


# User Retrieve
def retrieve_user():
    pass


# User Update
def update_user():
    pass


# User Delete
def delete_user():
    pass


# only for admins, somehow
# Product Create
def create_product():
    pass


# Product Retrieve
def retrieve_product():
    pass


# only for admins, somehow
# Product Update
def update_product():
    pass


# only for admins, somehow
# Product Delete
def delete_product():
    pass


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
