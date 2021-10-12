"""Contains all classes relateing to Parts."""

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, Index, DateTime
from sqlalchemy.orm import relationship
from fishbowl.database import Base, session
from fishbowl.database.baseclass import BaseType
from fishbowl.database.uom import Uom


class PartType(BaseType):
    """Represents a part type."""
    __tablename__ = 'parttype'

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default PartTypes."""
        data = [
            cls(id=10, name='Inventory'),
            cls(id=20, name='Service'),
            cls(id=21, name='Labor'),
            cls(id=22, name='Overhead'),
            cls(id=30, name='Non-Inventory'),
            cls(id=40, name='Internal Use'),
            cls(id=50, name='Capital Equipment'),
            cls(id=60, name='Shipping'),
            cls(id=70, name='Tax'),
            cls(id=80, name='Misc')
        ]
        session.add_all(data)
        session.commit()


class PartTrackingType(BaseType):
    """Represents a part tracking type."""
    __tablename__ = 'parttrackingtype'

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default PartTrackingTypes."""
        data = [
            cls(id=10, name='Text'),
            cls(id=20, name='Date'),
            cls(id=30, name='Expiration Date'),
            cls(id=40, name='Serial Number'),
            cls(id=50, name='Money'),
            cls(id=60, name='Quantity'),
            cls(id=70, name='Count'),
            cls(id=80, name='Checkbox'),
        ]
        session.add_all(data)
        session.commit()


class PartCategory(Base):
    """Represents a part category."""
    __tablename__ = 'partcategory'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String(255))

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default PartCategories."""
        data = [
            cls(name='General Class Of Parts', description='General')
        ]
        session.add_all(data)
        session.commit()


class Part(Base):
    """Represents a part."""
    __tablename__ = 'part'
    __table_args__ = (
        Index('ix_part_id', 'id'),
        Index('ix_part_num', 'num'),
    )
    
    id = Column(Integer, primary_key=True)
    abcCode = Column(String(1))
    accountingHash = Column(String(255))
    accountingId = Column(Integer)
    activeFlag = Column(Integer)
    adjustmentAccountId = Column(Integer)
    alertNote = Column(String(255))
    alwaysManufacture = Column(Boolean)
    cogsAccountId = Column(Integer)
    configurable = Column(Integer)
    controlledFlag = Column(Boolean)
    cycleCountTol = Column(DECIMAL(28, 9))
    dateCreated = Column(DateTime)
    dateLastModified = Column(DateTime)
    defaultBomId = Column(Integer, ForeignKey('bom.id'))
    defaultBomObj = relationship('Bom', foreign_keys=[defaultBomId])
    defaultProductId = Column(Integer, ForeignKey('product.id', name='FK_part_defaultProductId'), nullable=True)
    defaultProductObj = relationship('Product', backref='defaultProduct', foreign_keys=[defaultProductId])
    description = Column(String(255))
    details = Column(String(255))
    height = Column(DECIMAL(28, 9))
    inventoryAccountId = Column(Integer)
    lastChangedUser = Column(String(255))
    leadTime = Column(Integer)
    leadTimeToFulfill = Column(Integer)
    len = Column(DECIMAL(28, 9))
    num = Column(String(255))
    partClassId = Column(Integer)
    pickInUomOfPart = Column(Boolean)
    receivingTol = Column(DECIMAL(28, 9))
    revision = Column(Integer)
    scrapAccountId = Column(Integer)
    serializedFlag = Column(Integer)
    sizeUomId = Column(Integer, ForeignKey('uom.id'))
    sizeUomObj = relationship('Uom', backref='sizeUom', foreign_keys=[sizeUomId]) # type: Uom
    stdCost = Column(DECIMAL(28, 9))
    taxId = Column(Integer)
    trackingFlag = Column(Boolean)
    typeId = Column(Integer, ForeignKey('parttype.id'))
    typeObj = relationship('PartType', backref='partType') # type: PartType
    uomId = Column(Integer, ForeignKey('uom.id'))
    uomObj = relationship('Uom', backref='partUom', foreign_keys=[uomId]) # type: Uom
    upc = Column(String(255))
    url = Column(String(255))
    varianceAccountId = Column(Integer)
    weight = Column(DECIMAL(28, 9))
    weightUomId = Column(Integer, ForeignKey('uom.id'))
    weightUomObj = relationship('Uom', backref='weightUom', foreign_keys=[weightUomId]) # type: Uom
    width = Column(DECIMAL(28, 9))


class PartCost(Base):
    """Represents a part cost."""
    __tablename__ = 'partcost'
    __table_args__ = (
        Index('ix_partcost_partId', 'partId'),
    )
    
    
    id = Column(Integer, primary_key=True)
    avgCost = Column(DECIMAL(28, 9))
    dateCreated = Column(DateTime)
    dateLastModified = Column(DateTime)
    partId = Column(Integer, ForeignKey('part.id'))
    partObj = relationship('Part', backref='partCost') # type: Part
    qty = Column(DECIMAL(28, 9))
    totalCost = Column(DECIMAL(28, 9))


class PartReorder(Base):
    """Represents a part reorder point."""
    __tablename__ = 'partreorder'
    __table_args__ = (
        Index('ix_partreorder_partId', 'partId'),
        Index('ix_partreorder_locationGroupId', 'locationGroupId'),
    )
    
    id = Column(Integer, primary_key=True)
    locationGroupId = Column(Integer)
    orderUpToLevel = Column(DECIMAL(28, 9))
    partId = Column(Integer, ForeignKey('part.id'), unique=True)
    partObj = relationship('Part', backref='partReorder') # type: Part
    reorderPoint = Column(DECIMAL(28, 9))



class PartTracking(Base):
    """Represents part tracking."""
    __tablename__ = 'parttracking'
    __table_args__ = (
        Index('ix_parttracking_typeId', 'typeId'),
    )

    id = Column(Integer, primary_key=True)
    abbr = Column(String(255))
    activeFlag = Column(Integer)
    description = Column(String(255))
    name = Column(String(255), unique=True)
    sortOrder = Column(Integer)
    typeId = Column(Integer, ForeignKey('parttrackingtype.id'))
    typeObj = relationship('PartTrackingType', backref='partTracking') # type: PartTrackingType

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default PartTrackings."""
        data = [
            cls(id=1, abbr='Lot#', activeFlag=True, description='', name='Lot Number', sortOrder=1, typeObj=PartTrackingType.query.get(name='Text')),
            cls(id=2, abbr='Rev#', activeFlag=True, description='', name='Revision Level', sortOrder=2, typeObj=PartTrackingType.query.get(name='Text')),
            cls(id=3, abbr='ExpDate', activeFlag=True, description='', name='Expiration Date', sortOrder=3, typeObj=PartTrackingType.query.get(name='Expiration Date')),
            cls(id=4, abbr='SN(s)', activeFlag=True, description='', name='Serial Number', sortOrder=4, typeObj=PartTrackingType.query.get(name='Serial Number')),
        ]
        session.add_all(data)
        session.commit()


class PartToTracking(Base):
    """Represents a part to tracking."""
    __tablename__ = 'parttotracking'
    
    id = Column(Integer, primary_key=True)
    nextValue = Column(String(41))
    partId = Column(Integer, ForeignKey('part.id'))
    partObj = relationship('Part', backref='partToTracking') # type: Part
    partTrackingId = Column(Integer, ForeignKey('parttracking.id'))
    # TODO: Add PartTracking relationship
    # partTrackingObj = relationship('PartTracking', backref='partToTracking') # type: PartTracking
    primaryFlag = Column(Boolean)


class PartCostHistory(Base):
    """Stores historical part cost information."""
    __tablename__ = 'partcosthistory'

    id = Column(Integer, primary_key=True)
    avgCost = Column(DECIMAL(28, 9))
    dateCaptured = Column(DateTime)
    nextCost = Column(DECIMAL(28, 9))
    partId = Column(Integer, ForeignKey('part.id'))
    partObj = relationship('Part', backref='partCostHistory') # type: Part
    quantity = Column(DECIMAL(28, 9))
    stdCost = Column(DECIMAL(28, 9))
    totalCost = Column(DECIMAL(28, 9))
    
    @property
    def currentPerPartCost(self):
        return self.totalCost / self.quantity


# class PartAudit(Audit):
#     __tablename__ = 'part_aud'
#     __mapper_args__ = {'polymorphic_identity': 'part_aud'}