from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL, Boolean, Index
from sqlalchemy.orm import relationship
from fishbowl.database import Base, session
from fishbowl.database.baseclass import BaseType
from fishbowl.database.custom import CustomListItem
from fishbowl.database.uom import Uom
from fishbowl.database.part import Part
from fishbowl.database.user import User



class AutoCreateType(BaseType):
    """Represents an Auto Create Type for a Bill of Materials."""
    __tablename__ = 'bomtype'
    
    @classmethod
    def create_default_data(cls):
        """This function is used to create all default AutoCreateTypes."""
        data = [
            cls(id=10, name='Never'),
            cls(id=20, name='Order Quantity'),
            cls(id=25, name='Short Quantity'),
            cls(id=30, name='Always Create'),
            cls(id=40, name='Build to Order')
        ]
        session.add_all(data)
        session.commit()


class Bom(Base):
    """Represents a Bill of Materials."""
    __tablename__ = 'bom'
    __table_args__ = (
        Index('ix_bom_autoCreateTypeId', 'autoCreateTypeId'),
        Index('ix_bom_typeId', 'typeId'),
        Index('ix_bom_userId', 'userId')
    )
    
    id = Column(Integer, primary_key=True)
    activeFlag = Column(Boolean)
    autoCreateTypeId = Column(Integer, ForeignKey('bomtype.id'))
    autoCreateTypeObj = relationship('AutoCreateType', backref='bomAutoCreateType') # type: AutoCreateType
    configurable = Column(Boolean)
    dateCreated = Column(DateTime)
    dateLastModified = Column(DateTime)
    description = Column(String(255))
    estimatedDuration = Column(DECIMAL(28, 9))
    note = Column(String(255))
    num = Column(String(255))
    pickFromLocation = Column(Boolean)
    revision = Column(String(30))
    statisticsDateRange = Column(String(40))
    typeId = Column(Integer, ForeignKey('customlistitem.id'))
    typeObj = relationship('CustomListItem', backref='bomType') # type: CustomListItem
    url = Column(String(255))
    userId = Column(Integer, ForeignKey('sysuser.id'))
    userObj = relationship('User', backref='bomUser') # type: User


class BomItemGroup(Base):
    """Represents a Bom Item Group."""
    __tablename__ = 'bomitemgroup'
    __table_args__ = (
        Index('ix_bomitemgroup_bomId', 'bomId'),
    )
    
    id = Column(Integer, primary_key=True)
    bomId = Column(Integer, ForeignKey('bom.id'))
    bomObj = relationship('Bom', backref='bomItemGroupBom') # type: Bom
    name = Column(String(255), unique=True)
    prompt = Column(String(255))
    sortOrder = Column(Integer)


class BomItemType(BaseType):
    """Represents a Bom Item Type."""
    __tablename__ = 'bomitemtype'

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default BomItemTypes."""
        data = [
            cls(id=10, name='Finished Good'),
            cls(id=20, name='Raw Good'),
            cls(id=30, name='Repair Raw Good'),
            cls(id=31, name='Repair Finished Good'),
            cls(id=40, name='Note'),
            cls(id=50, name='Bill of Materials'),
        ]
        session.add_all(data)
        session.commit()


class BomItem(Base):
    """Represents an item in a Bom."""
    __tablename__ = 'bomitem'
    __table_args__ = (
        Index('ix_bomitem_bomId', 'bomId'),
        Index('ix_bomitem_bomItemGroupId', 'bomItemGroupId'),
        Index('ix_bomitem_partId', 'partId'),
        Index('ix_bomitem_typeId', 'typeId'),
        Index('ix_bomitem_uomId', 'uomId')
    )

    id = Column(Integer, primary_key=True)
    addToService = Column(Boolean)
    bomId = Column(Integer, ForeignKey('bom.id'))
    bomObj = relationship('Bom', backref='bomItemBom', foreign_keys=[bomId]) # type: Bom
    bomItemGroupId = Column(Integer, ForeignKey('bomitemgroup.id'))
    bomItemGroupObj = relationship('BomItemGroup', backref='bomItemBomGroup', foreign_keys=[bomItemGroupId]) # type: BomItemGroup
    description = Column(String(255))
    groupDefault = Column(Boolean)
    instructionNote = Column(String(255))
    instructionUrl = Column(String(255))
    maxQty = Column(DECIMAL(28, 9))
    minQty = Column(DECIMAL(28, 9))
    oneTimeItem = Column(Boolean)
    partId = Column(Integer, ForeignKey('part.id'))
    partObj = relationship('Part', backref='bomItemPart', foreign_keys=[partId]) # type: Part
    priceAdjustment = Column(DECIMAL(28, 9))
    quantity = Column(DECIMAL(28, 9))
    sortIdConfig = Column(Integer)
    sortIdInstruct = Column(Integer)
    stage = Column(String(255))
    stageBomId = Column(Integer, ForeignKey('bom.id'))
    stageBomObj = relationship('Bom', backref='bomItemStageBom', foreign_keys=[stageBomId]) # type: Bom
    typeId = Column(Integer, ForeignKey('bomitemtype.id'))
    typeObj = relationship('BomItemType', backref='bomItemType', foreign_keys=[typeId]) # type: BomItemType
    uomId = Column(Integer, ForeignKey('uom.id'))
    uomObj = relationship('Uom', backref='bomItemUom', foreign_keys=[uomId]) # type: Uom
    useItemLocation = Column(Boolean)
    variableQty = Column(Boolean)