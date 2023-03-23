from app import db
from datetime import datetime


# Define the User model
class User(db.Document):
    # Define the fields for the User model
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow, required=True)
    updated_at = db.DateTimeField(default=datetime.utcnow, required=True)
    
    # Define the method to convert User model to JSON
    def to_json(self):
        return {
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


# Define the Post model
class Post(db.Document):
    # Define the fields for the Post model
    title = db.StringField(max_length=120, required=True)
    content = db.StringField(required=True)
    author = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)
    created_at = db.DateTimeField(default=datetime.utcnow, required=True)
    updated_at = db.DateTimeField(default=datetime.utcnow, required=True)

    # Define the method to convert Post model to JSON
    def to_json(self):
        return {
            "title": self.title,
            "content": self.content,
            "author": self.author.to_json(),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
