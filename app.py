from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask.helpers import send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import sys

from database import connector
from model import entities

db = connector.Manager()
engine = db.create_engine()

app = Flask(__name__)
app.config.from_pyfile('config.py')

migrate = Migrate(app, db)


@app.route('/')
def index():
    return "Yay"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
