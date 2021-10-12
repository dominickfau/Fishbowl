from sqlalchemy import Column, Integer, String
from fishbowl.database import Base


class Vendor(Base):
    __tablename__ = 'vendor'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)