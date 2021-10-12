"""Contains all classes relateing to Custom fields."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from fishbowl.database import Base, session
from fishbowl.database.baseclass import BaseType


class CustomList(Base):
    """Represents a Custom List."""
    __tablename__ = 'customlist'

    id = Column(Integer, primary_key=True)
    description = Column(String(256), nullable=False)
    name = Column(String(40), nullable=False, unique=True)

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default CustomLists."""
        data = [
            cls(id=1, name='RMA Resolution', description='Resolution for the RMA Items.'),
            cls(id=2, name='RMA Issue', description='Reason for the RMA.'),
            cls(id=3, name='Bom Type', description='The type of BOM.')
        ]
        session.add_all(data)
        session.commit()


class CustomListItem(Base):
    """Represents an item in a Custom List."""
    __tablename__ = 'customlistitem'

    id = Column(Integer, primary_key=True)
    description = Column(String(256), nullable=False)
    listId = Column(Integer, ForeignKey('customlist.id'), nullable=False)
    listObj = relationship('CustomList', backref=backref('customlistitem', lazy=True))
    name = Column(String(40), nullable=False, unique=True)

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default CustomListItems."""
        data = [
            cls(id=1, name='Sent Replacement Parts', description='New finished parts sent back to customer.', listId=1),
            cls(id=2, name='Repaired RMA Items', description='RMA items repaired and sent back to customer.', listId=1),
            cls(id=3, name='RMA Items Scraped', description='Could not repair RMA Items.', listId=1),
            cls(id=4, name='Resolved', description='General resolution.', listId=1),
            cls(id=5, name='DOA', description='Part was dead on arrival.', listId=2),
            cls(id=6, name='Warranty', description='Part was returned for a warranty issue.', listId=2),
            cls(id=7, name='Shipping Damage', description='Parts damaged in shipping.', listId=2),
            cls(id=8, name='Manufacture', description='Make a Finished Part from a Raw Part.', listId=3),
            cls(id=9, name='Repair', description='Raw Parts used to fix a Finished Part.', listId=3),
            cls(id=10, name='Disassemble', description='Finished parts turned back into Raw Parts.', listId=3),
            cls(id=11, name='Service', description='', listId=3)
        ]
        session.add_all(data)
        session.commit()