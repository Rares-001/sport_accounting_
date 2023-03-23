from typing import List
from sqlalchemy.orm import Session
from models.user import User
from config import db_session


class UserService:
    def __init__(self, db_session: Session = db_session):
        self.db_session = db_session

    def get_user_by_id(self, user_id: int) -> User:
        user = self.db_session.query(User).filter_by(id=user_id).first()
        return user

    def get_user_by_email(self, email: str) -> User:
        user = self.db_session.query(User).filter_by(email=email).first()
        return user

    def create_user(self, name: str, email: str, password: str) -> User:
        new_user = User(name=name, email=email, password=password)
        self.db_session.add(new_user)
        self.db_session.commit()
        return new_user

    def update_user(self, user_id: int, name: str, email: str, password: str) -> User:
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            user.password = password
            self.db_session.commit()
        return user

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self.db_session.delete(user)
            self.db_session.commit()
            return True
        return False

    def get_all_users(self) -> List[User]:
        users = self.db_session.query(User).all()
        return users

