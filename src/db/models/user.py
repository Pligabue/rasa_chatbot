from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class User(Base):
    
    document = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    bills = relationship("Bill", back_populates="user")

    def __repr__(self):
        return f"<User(fullname='{self.first_name} {self.last_name}', document='{self.document}', email='{self.email}')>"