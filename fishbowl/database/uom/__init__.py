"""Contains all classes relateing to Unit of Measures."""

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, Index
from sqlalchemy.orm import relationship
from fishbowl.database import Base, session


class UomType(Base):
    """Represents a Uom type."""
    __tablename__ = 'uomtype'
    id = Column(Integer, primary_key=True)
    name = Column(String(15))


class Uom(Base):
    """Represents a Uom."""
    __tablename__ = 'uom'
    id = Column(Integer, primary_key=True)
    activeFlag = Column(Boolean, default=True)
    code = Column(String(10), nullable=False, unique=True)
    defaultRecord = Column(Boolean, default=False)
    description = Column(String(100), nullable=False)
    integral = Column(Boolean, default=False)
    name = Column(String(50), nullable=False, unique=True)
    readOnly = Column(Boolean, default=False)
    uomType = Column(Integer, ForeignKey('uomtype.id'))
    uomTypeObj = relationship('UomType', backref='uom') # type: UomType

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default Uoms."""
        data = [
            cls(code="ea", defaultRecord=True, description="A single item.", integral=True, name="Each", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Count').first()),
            cls(code="ft", description="Basic US unit of length.", name="Foot", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Length').first()),
            cls(code="lbs", description="Basic US unit of weight.", name="Pound", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Weight').first()),
            cls(code="hr", description="Basic unit of time.", name="Hour", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Time').first()),
            cls(code="gal", description="Basic US unit of liquid volume.", name="Gallon", uomTypeObj=UomType.query.filter_by(name='Volume').first()),
            cls(code="floz", description="US unit of liquid volume.", name="Fluid Ounce", uomTypeObj=UomType.query.filter_by(name='Volume').first()),
            cls(code="in", description="US unit of length.", name="Inch", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Length').first()),
            cls(code="kg", description="Metric unit of weight.", name="Kilogram", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Weight').first()),
            cls(code="oz", description="US unit of weight.", name="Ounce", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Weight').first()),
            cls(code="m", description="Basic metric unit of length.", name="Meter", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Length').first()),
            cls(code="L", description="Basic metric unit of liquid volume.", name="Liter", readOnly=True, uomTypeObj=UomType.query.filter_by(name='Volume').first()),
            cls(code="mm", description="1/1000 of a meter.", name="Millimeter", uomTypeObj=UomType.query.filter_by(name='Length').first()),
            cls(code="cm", description="1/100 of a meter.", name="Centimeter", uomTypeObj=UomType.query.filter_by(name='Length').first()),
            cls(code="km", description="1000 meters.", name="Kilometer", uomTypeObj=UomType.query.filter_by(name='Length').first()),
            cls(code="g", description="Metric unit of weight.", name="Gram", uomTypeObj=UomType.query.filter_by(name='Weight').first()),
            cls(code="mg", description="1/1000 of a gram.", name="Milligram", uomTypeObj=UomType.query.filter_by(name='Weight').first()),
            cls(code="mL", description="1/1000 of a Liter.", name="Milliliter", uomTypeObj=UomType.query.filter_by(name='Volume').first()),
            cls(code="min", description="1/60 of a hour.", name="Minute", uomTypeObj=UomType.query.filter_by(name='Time').first())
        ]
        session.add_all(data)
        session.commit()


class UomConversion(Base):
    """Represents how to convert from one Uom to another."""
    __tablename__ = 'uomconversion'
    __table_args__ = (
        Index('ix_uomconversion_fromUomId', 'fromUomId'),
    )


    id = Column(Integer, primary_key=True)
    description = Column(String(100))
    factor = Column(DECIMAL(28, 9),nullable=False)
    fromUomId = Column(Integer, ForeignKey('uom.id'), nullable=False)
    multiply = Column(DECIMAL(28, 9), nullable=False)
    toUomId = Column(Integer, ForeignKey('uom.id'), nullable=False)
    fromUomObj = relationship('Uom', backref='fromUom', foreign_keys=[fromUomId]) # type: Uom
    toUomObj = relationship('Uom', backref='toUom', foreign_keys=[toUomId]) # type: Uom

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default UomConversions."""
        data = [
            cls(description="1 Foot = 12 Inch", factor=12, fromUomObj=Uom.query.filter_by(code='ft').first(), multiply=1, toUomObj=Uom.query.filter_by(code='in').first()),
            cls(description="12 Inch = 1 Foot", factor=1, fromUomObj=Uom.query.filter_by(code='in').first(), multiply=12, toUomObj=Uom.query.filter_by(code='ft').first()),
            cls(description="1 Gallon = 128 Fluid Ounce", factor=128, fromUomObj=Uom.query.filter_by(code='gal').first(), multiply=1, toUomObj=Uom.query.filter_by(code='floz').first()),
            cls(description="128 Fluid Ounce = 1 Gallon", factor=1, fromUomObj=Uom.query.filter_by(code='floz').first(), multiply=128, toUomObj=Uom.query.filter_by(code='gal').first()),
            cls(description="1 Kilogram = 2.2046 Pound", factor=2.2046, fromUomObj=Uom.query.filter_by(code='kg').first(), multiply=1, toUomObj=Uom.query.filter_by(code='lbs').first()),
            cls(description="2.2046 Pound = 1 Kilogram", factor=1, fromUomObj=Uom.query.filter_by(code='lbs').first(), multiply=2.2046, toUomObj=Uom.query.filter_by(code='kg').first()),
            cls(description="1 Meter = 3.28084 Foot", factor=3.28084, fromUomObj=Uom.query.filter_by(code='m').first(), multiply=1, toUomObj=Uom.query.filter_by(code='ft').first()),
            cls(description="3.28084 Foot = 1 Meter", factor=1, fromUomObj=Uom.query.filter_by(code='ft').first(), multiply=3.28084, toUomObj=Uom.query.filter_by(code='m').first()),
            cls(description="1 Gallon = 3.7854 Liter", factor=3.7854, fromUomObj=Uom.query.filter_by(code='gal').first(), multiply=1, toUomObj=Uom.query.filter_by(code='l').first()),
            cls(description="3.7854 Liter = 1 Gallon", factor=1, fromUomObj=Uom.query.filter_by(code='l').first(), multiply=3.7854, toUomObj=Uom.query.filter_by(code='gal').first()),
            cls(description="1 Meter = 1000.0 Millimeter", factor=1000.0, fromUomObj=Uom.query.filter_by(code='m').first(), multiply=1, toUomObj=Uom.query.filter_by(code='mm').first()),
            cls(description="1000.0 Millimeter = 1 Meter", factor=1, fromUomObj=Uom.query.filter_by(code='mm').first(), multiply=1000.0, toUomObj=Uom.query.filter_by(code='m').first()),
            cls(description="1 Meter = 100.0 Centimeter", factor=100.0, fromUomObj=Uom.query.filter_by(code='m').first(), multiply=1, toUomObj=Uom.query.filter_by(code='cm').first()),
            cls(description="100.0 Centimeter = 1 Meter", factor=1, fromUomObj=Uom.query.filter_by(code='cm').first(), multiply=100.0, toUomObj=Uom.query.filter_by(code='m').first()),
            cls(description="1 Kilometer = 1000.0 Meter", factor=1000.0, fromUomObj=Uom.query.filter_by(code='km').first(), multiply=1, toUomObj=Uom.query.filter_by(code='m').first()),
            cls(description="1000.0 Meter = 1 Kilometer", factor=1, fromUomObj=Uom.query.filter_by(code='m').first(), multiply=1000.0, toUomObj=Uom.query.filter_by(code='km').first()),
            cls(description="1 Gram = 1000.0 Milligram", factor=1000.0, fromUomObj=Uom.query.filter_by(code='g').first(), multiply=1, toUomObj=Uom.query.filter_by(code='mg').first()),
            cls(description="1000.0 Milligram = 1 Gram", factor=1, fromUomObj=Uom.query.filter_by(code='mg').first(), multiply=1000.0, toUomObj=Uom.query.filter_by(code='g').first()),
            cls(description="1 Kilogram = 1000.0 Gram", factor=1000.0, fromUomObj=Uom.query.filter_by(code='kg').first(), multiply=1, toUomObj=Uom.query.filter_by(code='g').first()),
            cls(description="1000.0 Gram = 1 Kilogram", factor=1, fromUomObj=Uom.query.filter_by(code='g').first(), multiply=1000.0, toUomObj=Uom.query.filter_by(code='kg').first()),
            cls(description="1 Liter = 1000.0 Milliliter", factor=1000.0, fromUomObj=Uom.query.filter_by(code='l').first(), multiply=1, toUomObj=Uom.query.filter_by(code='ml').first()),
            cls(description="1000.0 Milliliter = 1 Liter", factor=1, fromUomObj=Uom.query.filter_by(code='ml').first(), multiply=1000.0, toUomObj=Uom.query.filter_by(code='l').first()),
            cls(description="1 Inch = 25.4 Millimeter", factor=25.4, fromUomObj=Uom.query.filter_by(code='in').first(), multiply=1, toUomObj=Uom.query.filter_by(code='mm').first()),
            cls(description="25.4 Millimeter = 1 Inch", factor=1, fromUomObj=Uom.query.filter_by(code='mm').first(), multiply=25.4, toUomObj=Uom.query.filter_by(code='in').first()),
            cls(description="1 Pound = 453.59237 Gram", factor=453.59237, fromUomObj=Uom.query.filter_by(code='lbs').first(), multiply=1, toUomObj=Uom.query.filter_by(code='g').first()),
            cls(description="453.59237 Gram = 1 Pound", factor=1, fromUomObj=Uom.query.filter_by(code='g').first(), multiply=453.59237, toUomObj=Uom.query.filter_by(code='lbs').first()),
            cls(description="1 Pound = 453592.37 Milligram", factor=453592.37, fromUomObj=Uom.query.filter_by(code='lbs').first(), multiply=1, toUomObj=Uom.query.filter_by(code='mg').first()),
            cls(description="453592.37 Milligram = 1 Pound", factor=1, fromUomObj=Uom.query.filter_by(code='mg').first(), multiply=453592.37, toUomObj=Uom.query.filter_by(code='lbs').first()),
            cls(description="1 Pound = 16.000 Ounce", factor=16.000, fromUomObj=Uom.query.filter_by(code='lbs').first(), multiply=1, toUomObj=Uom.query.filter_by(code='oz').first()),
            cls(description="16.000 Ounce = 1 Pound", factor=1, fromUomObj=Uom.query.filter_by(code='oz').first(), multiply=16.000, toUomObj=Uom.query.filter_by(code='lbs').first()),
            cls(description="1 Hour = 60.0 min", factor=60.0, fromUomObj=Uom.query.filter_by(code='hr').first(), multiply=1, toUomObj=Uom.query.filter_by(code='min').first()),
            cls(description="60.0 min = 1 Hour", factor=1, fromUomObj=Uom.query.filter_by(code='min').first(), multiply=60.0, toUomObj=Uom.query.filter_by(code='hr').first())
        ]
        session.add_all(data)
        session.commit()