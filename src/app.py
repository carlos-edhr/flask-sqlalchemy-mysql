# Imports
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Python app
app = Flask(__name__)

# DB connection
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/flaskmysql'
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

    print(request.json)
    return 'received'


if __name__ == "__main__":
    app.run(debug=True)
