# Import the Flask application instance from the main package
from app import create_app, db

# Import the Flask-Testing library for testing the application
from flask_testing import TestCase

# Define a base test case class that all other test cases will inherit from
class BaseTestCase(TestCase):

    def create_app(self):
        """
        Create an instance of the Flask application for testing purposes.

        Returns:
            app (Flask): The Flask application instance.
        """
        app = create_app('testing')
        return app

    def setUp(self):
        """
        Set up the test database before each test.
        """
        db.create_all()

    def tearDown(self):
        """
        Tear down the test database after each test.
        """
        db.session.remove()
        db.drop_all()
