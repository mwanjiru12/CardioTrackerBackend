from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = "bY\xf1Xz\x01\xad|eQ\x80t \xca\x1a\x10K"

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)
    migrate.init_app(app, db)

    # Initialize CORS (allowing from localhost:4000)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:4000", "http://192.168.100.99:4000"]}}, supports_credentials=True)

    # Import and register routes
    from .routes import auth, active_days, activities
    app.register_blueprint(auth.bp)  
    app.register_blueprint(active_days.bp)
    app.register_blueprint(activities.bp)

    return app