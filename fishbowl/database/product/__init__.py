"""Contains all classes relateing to Products."""

import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, DateTime
from sqlalchemy.orm import relationship
from fishbowl.database import Base
from fishbowl.database.part import Part
from fishbowl.database.uom import Uom


class Product(Base):
    """Represents a product."""
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    activeFlag = Column(Integer, nullable=False, default=True)
    alertNote = Column(String(255))
    cartonCount = Column(DECIMAL(28, 9), nullable=False, default=0.0)
    # defaultCartonTypeId = Column(Integer, ForeignKey('cartontype.id'))
    # TODO: Add defaultCartonType relationship.
    # defaultCartonTypeObj = relationship('CartonType', foreign_keys=[defaultCartonTypeId]) # type: CartonType
    dateCreated = Column(DateTime, nullable=False, default=datetime.datetime.now())
    dateLastModified = Column(DateTime, nullable=False, default=datetime.datetime.now())
    defaultSoItemType = Column(String(255), nullable=False)
    description = Column(String(255))
    details = Column(String(255))
    # displayTypeId = Column(Integer, ForeignKey('kitdisplaytype.id'))
    # TODO: Add displayType relationship.
    # displayTypeObj = relationship('DisplayType', foreign_keys=[displayTypeId]) # type: KitDisplayType
    height = Column(DECIMAL(28, 9))
    kitFlag = Column(Integer, nullable=False, default=False)
    kitGroupedFlag = Column(Integer, nullable=False, default=False)
    len = Column(DECIMAL(28, 9))
    num = Column(String(255), nullable=False, unique=True)
    partId = Column(Integer, ForeignKey('product.id', name='FK_product_partId'), nullable=False)
    partObj = relationship('Part', foreign_keys=[partId], backref='productToPart', primaryjoin='Product.partId == Part.id') # type: Part
    price = Column(DECIMAL(28, 9))
    sellableInOtherUoms = Column(Integer, nullable=False, default=False)
    showSoComboFlag = Column(Integer, nullable=False, default=False)
    sizeUomId = Column(Integer, ForeignKey('uom.id'))
    sizeUomObj = relationship('Uom', foreign_keys=[sizeUomId]) # type: Uom
    sku = Column(String(255))
    # taxId = Column(Integer, ForeignKey('tax.id'))
    # TODO: Add tax relationship.
    # taxObj = relationship('Tax', foreign_keys=[taxId]) # type: Tax
    taxableFlag = Column(Integer, nullable=False, default=False)
    uomId = Column(Integer, ForeignKey('uom.id'), nullable=False)
    uomObj = relationship('Uom', foreign_keys=[uomId]) # type: Uom
    upc = Column(String(255))
    url = Column(String(255))
    usePriceFlag = Column(Boolean)
    weight = Column(DECIMAL(28, 9))
    weightUomId = Column(Integer, ForeignKey('uom.id'))
    weightUomObj = relationship('Uom', foreign_keys=[weightUomId]) # type: Uom
    width = Column(DECIMAL(28, 9))