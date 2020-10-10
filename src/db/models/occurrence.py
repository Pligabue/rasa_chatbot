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

    def address(self):
        return self.power_supply.address

    def status_is(self, status):
        return self.status == status

    def category_is(self, category):
        return self.category == category

    def has_estimation(self):
        return self.estimated_end_time is not None

    def time_until_estimation(self):
        return self.estimated_end_time - datetime.now()

    @validates('category')
    def validate_category(self, key, category):
        assert category in ["power_outage", "maintenance"]
        return category

    @validates('status')
    def validate_status(self, key, status):
        assert status in ["pending", "in_progress", "done", "cancelled"]
        return status

    def __repr__(self):
        return f"<Occurrence(category='{self.category}', " \
               f"status='{self.status}', start_time={self.start_time}, " \
               f"end_time={self.end_time} " \
               f"estimated_end_time={self.estimated_end_time})>"
