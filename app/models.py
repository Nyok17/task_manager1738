from app.extensions import db
from datetime import datetime, timezone


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=True)
    tasks = db.relationship('Task', backref='owner', lazy=True)

    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
