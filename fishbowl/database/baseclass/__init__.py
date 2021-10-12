from sqlalchemy import Column, Integer, String

from fishbowl.database import Base


class BaseType(Base):
    """Base class for type tables."""
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)