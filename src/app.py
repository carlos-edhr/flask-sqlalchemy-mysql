# Imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Python app
app = Flask(__name__)

# DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sonata09X!@localhost/flaskmysql?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ORM
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description


db.create_all()

# Database Schema


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# Routes
@app.route('/tasks', methods=['POST'])
def create_task():

    title = request.json['title']
    description = request.json['description']

    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)

    return 'received'


@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result)


@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):


if __name__ == "__main__":
    app.run(debug=True)
