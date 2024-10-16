from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuration settings
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from models import Episode, Guest, Appearance  # Ensure this matches your models' module

    # Register routes
    #from routes import *  # Import your routes from a separate routes file
    
    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Create the database and tables if they don't exist
        db.create_all()
    
    app.run(debug=True)

