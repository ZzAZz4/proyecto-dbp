from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask.helpers import send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import sys
from database import connector

app = Flask(__name__)
app.config.from_pyfile('config.py')

"""
db = connector.Manager()
engine = db.createEngine()
"""

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# @app.route('/create', methods=['POST'])
# def create_todo_post():
#     print("creating todo using POST form")
#     description = request.form.get('description', '**description no encontrada**')
#     todo = Todo(description=description)
#     db.session.add(todo)
#     db.session.commit()
#     return redirect(url_for('index'))


# @app.route('/create', methods=['GET'])
# def create_todo_get():
#     print("creating todo using GET form")
#     description = request.args.get('description', '**description no encontrada**')
#     todo = Todo(description=description)
#     db.session.add(todo)
#     db.session.commit()
#     return redirect(url_for('index'))


# @app.route('/todos/create2', methods=['POST'])
# def create_todo_json():
#     data_string = request.data
#     data_dictionary = json.loads(data_string)
#     description = data_dictionary['description']
#     todo = Todo(description=description)
#     db.session.add(todo)
#     db.session.commit()
#     return jsonify(
#         description=todo.description
#     )


# @app.route('/todos/create', methods=['POST'])
# def create_todo():
#     response = {}
#     error = False
#     try:
#         description = request.get_json()['description']
#         todo = Todo(description=description)
#         db.session.add(todo)
#         db.session.commit()
#         response['description'] = todo.description
#         response['id'] = todo.id
#     except:
#         error = True
#         db.session.rollback()
#         print(sys.exc_info())
#     finally:
#         db.session.close()

#     if error:
#         response['error_message'] = '[BE] Something went wrong!'
#     response['error'] = error
#     return jsonify(response)


# @app.route('/search/<todo_id>', methods=['GET'])
# def search_by_id(todo_id):
#     todo = Todo.query.get(todo_id)
#     return 'The description is: ' + todo.description


# @app.route('/todos/<todo_id>/set-completed', methods=['POST'])
# def update_completed_by_id(todo_id):
#     response = {}
#     error = False
#     try:
#         todo = Todo.query.get_or_404(todo_id)
#         if todo is None:
#             response['error_message'] = todo_id + ' not found in database!'
#         new_completed = request.get_json()['completed']
#         todo.completed = new_completed
#         db.session.commit()
#     except:
#         error = True
#         db.session.rollback()
#     finally:
#         db.session.close()

#     if error:
#         response['error_message2'] = 'something went wrong updating!'
#     return jsonify(response)


# @app.route('/todos/<todo_id>/delete-todo', methods=['DELETE'])
# def delete_todo_by_id(todo_id):
#     response = {}
#     error = False
#     try:
#         todo = Todo.query.get_or_404(todo_id)
#         if todo is None:
#             response['error_message'] = todo_id + ' not found in database.'
#         db.session.delete(todo)
#         db.session.commit()
#     except:
#         error = True
#         db.session.rollback()
#     finally:
#         db.session.close()

#     response['success'] = error
#     return jsonify(response)


@app.route('/')
def index():
    return "Yay"


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=5002, debug=True)
