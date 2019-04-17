from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ParkTwo(Base):
    __tablename__  = 'park_two'
    park_id = Column(Integer, primary_key=True)
    inside = Column(Integer, default=None, nullable=True)
    license_number = Column(String(10), nullable=True)
    create_time = Column(DateTime, onupdate=True, nullable=True)


class OpenOrder(Base):
    __tablename__ = 'open_order'
    order_id = Column(Integer, primary_key=True)
    order = Column(Integer, default=0)
