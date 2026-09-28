from flask import Flask, jsonify
from app.config import Config
from app.extensions import db, marsh, bcrypt, jwt



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    marsh.init_app(app)

    #import and register blueprints later
    from .auth import init_auth_module
    from .tasks import init_tasks_module

    init_auth_module(app)
    init_tasks_module(app)



    #Error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"message": "Bad Request"}), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"message": "Unauthorized"}), 401
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"message": "Resource Not Found"})
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"message": "Internal error"})

    return app