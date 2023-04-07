import os


class Config:
    # Set a default value for SECRET_KEY and retrieve it from the environment variables if available
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'quintor-project-accounting-sports-a1b2c3'
    if SECRET_KEY is None:
        raise ValueError('You must set the SECRET_KEY environment variable')

    # Set the database URI
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/sport_accounting'

    # Disable modification tracking to reduce overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
