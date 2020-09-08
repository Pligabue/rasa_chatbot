from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class Bill(Base):

    user_id = Column(Integer, ForeignKey('users.id'))
    value = Column(Float)
    paid = Column(Boolean, default=False)
    due_date = Column(Date)

    user = relationship("User", back_populates="bills")

    def __repr__(self):
        return f"<Bill(user='user_document='{self.user.document}' paid={self.paid} due_date={self.due_date})>"