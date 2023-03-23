import os

# Define the base directory of the application.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    The base configuration for the application.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    # Set the MongoDB database URI.
    MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/myapp'
    # Set the PostgreSQL database URI.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/myapp'
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
