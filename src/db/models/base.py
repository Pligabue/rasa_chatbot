from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

import re

class Mixin(object):

    @declared_attr
    def __tablename__(cls):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower() + ("s" if cls.__name__[-1] != "s" else "es")

    id =  Column(Integer, primary_key=True)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def from_dict(self, data_dict):
        for key, value in data_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)

Base = declarative_base(cls=Mixin)