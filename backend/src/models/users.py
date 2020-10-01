from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from .models import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(), nullable=False, unique=True)
    first_name = Column(String())
    last_name = Column(String())
    role = Column(String())
    created_at = Column(DateTime)
    completed = Column(Boolean, nullable=False)

    def __init__(self, user_id):
        self.user_id = user_id
        self.role = "customer"
        self.created_at = datetime.utcnow()
        self.completed = False

    def format(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role,
            "created_at": self.created_at,
            "verified": self.completed
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
