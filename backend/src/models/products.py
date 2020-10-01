from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from .models import db


class Product(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(Float(2), nullable=False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    seller = relationship("User", backref=backref("products", cascade="all, delete-orphan"))
    category = relationship("Category", backref=backref("products", cascade="all, delete-orphan"))

    def __init__(self, name, price, seller_id=0, category_id=1, quantity=1):
        self.name = name
        self.price = price
        self.seller_id = seller_id
        self.category_id = category_id
        self.quantity = quantity

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "seller_id": self.seller_id,
            "category_id": self.category_id,
            "quantity": self.quantity
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
