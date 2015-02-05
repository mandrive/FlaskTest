from sqlalchemy.orm import sessionmaker
from flaskTest import AppConfig
from flaskTest.dbmodels.Models import User, Post


class BaseService():
    __dbEngine = None
    __session = None

    def __init__(self, dbEngine=None):
        if dbEngine is None:
            self.__dbEngine = AppConfig.DBENGINE
        else:
            self.__dbEngine = dbEngine
        Session = sessionmaker(bind=self.__dbEngine)
        self.__session = Session()

    def get_session(self):
        return self.__session


class PostService(BaseService):
    def __init__(self):
        super(PostService, self).__init__()

    def getAll(self):
        return self.get_session().query(Post)

    def getById(self, id):
        return self.get_session().query(Post).filter_by(id=id).first()


class UserService(BaseService):
    def __init__(self):
        super(UserService, self).__init__()

    def getUserByUsername(self, username):
        user = self.get_session().query(User).filter_by(username=username).first()
        return user

    def getAll(self):
        return self.get_session().query(User)

    def validate(self, username, password):
        user = self.getAll().filter_by(username=username, password=password).first()
        if user is not None:
            return True
        return False