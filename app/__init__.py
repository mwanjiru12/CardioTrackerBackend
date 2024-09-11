from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()  # Initialize Migrate without app and db instances

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = "b'Y\xf1Xz\x01\xad|eQ\x80t \xca\x1a\x10K'"

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)

    # Initialize Migrate with app and db instances
    migrate.init_app(app, db)

    # Import routes
    from .routes import auth, active_days
    app.register_blueprint(auth.bp)
    # app.register_blueprint(users.bp)
    # app.register_blueprint(activities.bp)
    app.register_blueprint(active_days.bp)

    return app