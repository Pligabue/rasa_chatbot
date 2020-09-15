from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from datetime import datetime

from .base import Base

class Occurrence(Base):
    
    power_supply_id = Column(Integer, ForeignKey('power_supplies.id'))

    start_time = Column(DateTime)
    end_time = Column(DateTime)
    estimated_end_time = Column(DateTime)
    category = Column(String)
    description = Column(Text)
    status = Column(String)

    power_supply = relationship("PowerSupply", back_populates="occurrences")
    
    def is_solved(self):
        return self.status == "solved"

    @validates('category')
    def validate_category(self, key, category):
        assert category in ["power_outage", "maintenance"]
        return category

    @validates('status')
    def validate_status(self, key, status):
        assert status in ["in_progress", "done", "cancelled"]
        return status

    def __repr__(self):
        return f"<Occurrence(category='{self.category}', status='{self.status}', start_time={self.start_time}, end_time={self.end_time} estimated_end_time={self.estimated_end_time})>"
