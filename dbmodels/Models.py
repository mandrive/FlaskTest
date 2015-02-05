from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    title = Column(String)
    createDate = Column(DateTime)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(username='%s', password='%s')>" % (self.username, self.password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id