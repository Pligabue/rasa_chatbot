from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base


class User(Base):

    address_id = Column(Integer, ForeignKey('addresses.id'))

    document = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)

    bills = relationship("Bill", back_populates="user")
    address = relationship("Address", back_populates="users")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<User(fullname='{self.full_name()}', " \
               f"document='{self.document}', email='{self.email}'), " \
               f"phone_number={self.phone_number}>"
