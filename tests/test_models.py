import unittest
from app import create_app, db
from app.models import User, Post

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test function runs.
        It creates a new Flask app instance, sets some app configurations, and initializes a new in-memory database.
        """
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """
        This method is called after each test function runs.
        It removes the in-memory database and pops the Flask app context.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        """
        This is a test function that tests the password hashing functionality of the User model.
        It creates a new user with a password, hashes the password, and compares it to the stored password hash.
        """
        u = User(username='john')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_follow(self):
        """
        This is a test function that tests the follow/unfollow functionality of the User model.
        It creates two users, has one user follow the other, and checks that the first user is following the second user.
        It then has the first user unfollow the second user and checks that they are no longer following each other.
        """
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add_all([u1, u2])
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0))

    def test_follow_posts(self):
        """
        This is a test function that tests the functionality of the followed_posts() method of the User model.
        It creates two users and two posts, has one user follow the other, and checks that the followed_posts()
        method returns the correct posts.
        """
        # create users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add_all([u1, u2])

        # create posts
        now = datetime.utcnow()
        p1 = Post(body="post from john", author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from mary", author=u2,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from david", author=u1,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
       
    def test_password_reset_token(self):
        """
        This is a test function that tests the password reset token functionality of the User model.
        It creates a new user and generates a password reset token for them.
        It then verifies that the token is valid and returns the correct user.
        """
        u = User(username='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()

        token = u.get_reset_password_token()
        self.assertIsNotNone(token)

        user = User.verify_reset_password_token(token)
        self.assertEqual(user, u)

    def test_avatar(self):
        """
        This is a test function that tests the avatar generation functionality of the User model.
        It creates a new user with an email address and verifies that the user's avatar URL is correct.
        """
        u = User(username='john', email='john@example.com')
        avatar = u.avatar(128)
        expected_url = 'https://www.gravatar.com/avatar/' + \
                       'd4c74594d841139328695756648b6bd6' + \
                       '?d=identicon&s=128'
        self.assertEqual(avatar[0: len(expected_url)], expected_url)
