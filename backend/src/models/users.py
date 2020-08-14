from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .models import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(), nullable=False)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    role = Column(String(), nullable=False, default="customer")
    created_at = Column(DateTime)

    def format(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role,
            "created_at": self.created_at
        }

    def insert(self):
        self.created_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
