from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), default='https://bacanhem.vn/Design/man.png')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://cdn.tgdd.vn/Products/Images/42/299033/iphone-15-pro-black-thumbnew-600x600.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), user_role=UserRoleEnum.ADMIN)
        db.session.add(u)
        db.session.commit()


        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')
        c3 = Category(name='Desktop')
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()
        p1 = Product(name='iphone 13', price='20000000', category_id=1)
        p2 = Product(name='Galaxy Tab S9', price='28000000', category_id=2)
        p3 = Product(name='iPad Pro 2023', price='21000000', category_id=2)
        p4 = Product(name='Galaxy S23', price='18000000', category_id=1)
        p5 = Product(name='iphone 15', price='22000000', category_id=1)
        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
