import unittest
from app import create_app, db
from app.models import User

class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test function runs.
        It creates a new Flask app instance, sets some app configurations, and initializes a new in-memory database.
        """
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        """
        This method is called after each test function runs.
        It removes the in-memory database and pops the Flask app context.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        """
        This is a test function that tests the functionality of the home page route ('/').
        It makes a GET request to the home page route and checks that the response status code is 200.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        """
        This is a test function that tests the functionality of the register page route ('/auth/register').
        It makes a GET request to the register page route and checks that the response status code is 200.
        """
        response = self.client.get('/auth/register')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """
        This is a test function that tests the functionality of the login page route ('/auth/login').
        It makes a GET request to the login page route and checks that the response status code is 200.
        """
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """
        This is a test function that tests the functionality of the logout route ('/auth/logout').
        It creates a new user, logs the user in, and then logs the user out.
        It checks that the user is no longer authenticated by making a GET request to the home page route ('/') and checking that the response status code is 302.
        """
        # create user
        u = User(username='john', email='john@example.com')
        u.set_password('cat')
        db.session.add(u)
        db.session.commit()

        # log user in
        response = self.client.post('/auth/login', data={
            'username': 'john',
            'password': 'cat'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('You have been logged in' in response.data)

        # log user out
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('You have been logged out' in response.data)

        # check that user is logged out
        response = self.client.get('/')
        self.assertEqual(response.status_code,
        
        # check that user is logged out and redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertTrue('href="/auth/login"' in response.data)
