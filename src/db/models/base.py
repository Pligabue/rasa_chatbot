from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

class Mixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"

    id =  Column(Integer, primary_key=True)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

Base = declarative_base(cls=Mixin)