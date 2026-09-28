from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, current_user
from ..models import Task
from .schemas import TaskSchema
from app.extensions import db

tasks_bp = Blueprint('tasks', __name__)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@tasks_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.filter_by(user_id = current_user.id).all()
    return tasks_schema.jsonify(tasks)


@tasks_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return task_schema.jsonify(task)

@tasks_bp.route('/add_task', methods=['POST'])
@jwt_required()
def add_tasks():
    """A function to add tasks"""
    data = task_schema.load(request.json)
    task = Task(
        title = data['title'],
        description = data.get('description'),
        date_created = data.get('date_created'),
        user_id = current_user.id
    )

    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task added successfully"})

@tasks_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user).first()
    if not task:
        return jsonify({"error": "Task not found"})
    data = task_schema.load(request.json)

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.date_created = data.get('date_created', task.date_created)

    db.session.commit()
    return jsonify({"message": "Task updated successfully"})

@tasks_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200

