# app/tasks/__init__.py
from .routes import tasks_bp

def init_tasks_module(app):
    """Initialize tasks module"""
    app.register_blueprint(tasks_bp)
    # Add any task-specific initialization here

__all__ = ['tasks_bp', 'init_tasks_module']