from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from itsdangerous import URLSafeTimedSerializer
from enum import Enum

import AppConfig


Base = declarative_base()

login_serializer = URLSafeTimedSerializer(AppConfig.APPSECRETKEY)


class UserPrivileges(Enum):
    USER = 1
    ADMIN = 2


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    title = Column(String)
    createDate = Column(DateTime)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    type = Column(Integer)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<User(username='%s', password='%s')>" % (self.username, self.password)

    def is_admin(self):
        return UserPrivileges(self.type) == UserPrivileges.ADMIN

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_auth_token(self):
        data = [str(self.id), self.password]
        return login_serializer.dumps(data)