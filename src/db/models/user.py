from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class User(Base):
    
    power_supply_id = Column(Integer, ForeignKey('power_supplies.id'))
    address_id = Column(Integer, ForeignKey('addresses.id'))

    document = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    bills = relationship("Bill", back_populates="user")
    power_supply = relationship("PowerSupply", back_populates="users")
    address = relationship("Address", back_populates="users")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<User(fullname='{self.first_name} {self.last_name}', document='{self.document}', email='{self.email}')>"