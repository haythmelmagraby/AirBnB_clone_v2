#!/usr/bin/python3
"""DBStorage Module"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """DBStorage Class"""
    __engine = None
    __session = None
    def __init__(self):
        """Initializatin"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(Amenity).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Review).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, obj.id): obj for obj in objects}

    def new(self, obj):
        """add objects to current db"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """delete objects from session"""
        if obj is not None:
            self.__session.delete(obj)

    def save(self):
        """save db session"""
        self.__session.commit()

    def reload(self):
        """create db tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close db session"""
        self.__session.close()
