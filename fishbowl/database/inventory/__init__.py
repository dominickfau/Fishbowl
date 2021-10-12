"""Contains all classes relateing to Inventory."""


import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from fishbowl.database import Base
from fishbowl.database.baseclass import BaseType
from fishbowl.database.customer import Customer
from fishbowl.database.vendor import Vendor


class LocationType(BaseType):
    """Represents a location type."""
    __tablename__ = 'locationtype'

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default LocationTypes."""
        data = [
            cls(name="Consignment"),
            cls(name="In Transit"),
            cls(name="Inspection"),
            cls(name="Locked"),
            cls(name="Manufacturing"),
            cls(name="Picking"),
            cls(name="Receiving"),
            cls(name="Shipping"),
            cls(name="Stock"),
            cls(name="Store Front"),
            cls(name="Vendor")
        ]


class LocationGroup(Base):
    """Represents a location group."""
    __tablename__ = 'locationgroup'
    
    id = Column(Integer, primary_key=True)
    activeFlag = Column(Boolean, nullable=False)
    dateLastModified = Column(DateTime, default=datetime.datetime.now())
    name = Column(String(255), nullable=False, unique=True)


class Location(Base):
    """Represents a location for parts."""
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    activeFlag = Column(Boolean)
    countedAsAvailable = Column(Boolean)
    dateLastModified = Column(DateTime, default=datetime.datetime.now())
    defaultCustomerId = Column(Integer, ForeignKey('customer.id'), nullable=True)
    defaultCustomerObj = relationship('Customer', backref='location') # type: Customer
    defaultFlag = Column(Boolean)
    defaultVendorId = Column(Integer, ForeignKey('vendor.id'), nullable=True)
    defaultVendorObj = relationship('Vendor', backref='location') # type: Vendor
    description = Column(String(255))
    locationGroupId = Column(Integer, ForeignKey('locationgroup.id'), nullable=False)
    locationGroupObj = relationship('LocationGroup', backref='location') # type: LocationGroup
    name = Column(String(255), nullable=False, unique=True)
    pickable = Column(Boolean)
    receivable = Column(Boolean)
    sortOrder = Column(Integer)
    typeId = Column(Integer, ForeignKey('locationtype.id'), nullable=False)
    typeObj = relationship('LocationType', backref='location') # type: LocationType