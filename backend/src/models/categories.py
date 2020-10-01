from sqlalchemy import Column, Integer, String
from .models import db


class Category(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    category = Column(String(), nullable=False)

    def __init__(self, category):
        self.category = category

    def format(self):
        return {
            "id": self.id,
            "category": self.category
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
