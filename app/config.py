import os

# Define the base directory of the application.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    The base configuration for the application.
    """
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    
    # Set the MongoDB database URI.
    MONGODB_URI = 'mongodb+srv://Rares:admin@cluster0.y9osbya.mongodb.net/test'

    # Set the PostgreSQL database URI.
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/sport_accounting'

    
    # Set to False to disable database modification tracking.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    The configuration for the development environment.
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    The configuration for the production environment.
    """
    DEBUG = False
