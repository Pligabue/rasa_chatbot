from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base


class Address(Base):

    country = Column(String)
    state = Column(String)
    city = Column(String)
    neighbourhood = Column(String)
    street = Column(String)
    number = Column(String)
    postal_code = Column(String)

    users = relationship("User", back_populates="address")
    power_supply = relationship("PowerSupply", back_populates="address")

    def __repr__(self):
        return f"<Address(country='{self.country}', state='{self.state}', " \
               f"city='{self.city}, postal_code={self.postal_code}')>"
