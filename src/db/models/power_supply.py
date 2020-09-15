from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from datetime import datetime

from .base import Base

class PowerSupply(Base):
    
    __tablename__ = "power_supplies"

    address_id = Column(Integer, ForeignKey('addresses.id'))

    description = Column(Text)
    status = Column(String)

    occurrences = relationship("Occurrence", back_populates="power_supply", order_by="desc(Occurrence.start_time)", lazy="dynamic")
    address = relationship("Address", back_populates="power_supply")
    users = relationship("User", back_populates="power_supply")

    @validates('status')
    def validate_status(self, key, status):
        assert status in ["up", "down"]
        return status

    def __repr__(self):
        return f"<Occurrence(category='{self.category}', status='{self.status}')>"
