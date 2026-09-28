import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'smellycatsmellycat'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///task_manager.db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'heyjude'