import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SSECRET_KEY = os.environ.get('SECRET_KEY', 'my_very_strong_secret_key')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/sport_accounting'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
