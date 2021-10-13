from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from fishbowl.database import Base, session
from fishbowl.database.baseclass import BaseType
from fishbowl.database.user import User
from fishbowl.database.customer import Customer
from fishbowl.database.product import Product
from fishbowl.database.uom import Uom


class SalesOrderStatus(BaseType):
    __tablename__ = 'sostatus'


class SalesOrderType(BaseType):
    __tablename__ = 'sotype'


class SalesOrderItemStatus(BaseType):
    __tablename__ = 'soitemstatus'


class SalesOrderItemType(BaseType):
    __tablename__ = 'soitemtype'


class SalesOrder(Base):
    __tablename__ = 'so'

    id = Column(Integer, primary_key=True)
    billToAddress = Column(String(90))
    billToCity = Column(String(30))
    billToCountryId = Column(Integer)
    billToName = Column(String(40))
    billToStateId = Column(Integer)
    billToZip = Column(String(10))
    carrierId = Column(Integer)
    carrierServiceId = Column(Integer)
    cost = Column(DECIMAL(28, 9))
    currencyId = Column(Integer)
    currencyRate = Column(DECIMAL(28, 9))
    customerContact = Column(String(256))
    customerId = Column(Integer, ForeignKey('customer.id'))
    customerObj = relationship('Customer', backref='customer') # type: Customer
    customerPO = Column(String(25))
    dateCompleted = Column(DateTime)
    dateCreated = Column(DateTime)
    dateExpired = Column(DateTime)
    dateFirstShip = Column(DateTime)
    dateIssued = Column(DateTime)
    dateLastModified = Column(DateTime)
    dateRevision = Column(DateTime)
    email = Column(String(256))
    estimatedTax = Column(DECIMAL(28, 9))
    locationGroupId = Column(Integer)
    note = Column(String(256))
    num = Column(String(25))
    paymentTermsId = Column(Integer)
    phone = Column(String(256))
    priorityId = Column(Integer)
    shipToResidential = Column(Integer)
    revisionNum = Column(Integer)
    salesman = Column(String(100))
    salesmanId = Column(Integer)
    salesmanInitials = Column(String(5))
    shipTermsId = Column(Integer)
    shipToAddress = Column(String(255))
    shipToCity = Column(String(255))
    shipToCountryId = Column(Integer)
    shipToName = Column(String(255))
    shipToStateId = Column(Integer)
    shipToZip = Column(String(255))
    statusId = Column(Integer, ForeignKey('sostatus.id'))
    statusObj = relationship('SalesOrderStatus', backref='sostatus', foreign_keys=[statusId]) # type: SalesOrderStatus
    taxRate = Column(DECIMAL(28, 9))
    taxRateId = Column(Integer)
    taxRateName = Column(String(30))
    toBeEmailed = Column(Boolean)
    toBePrinted = Column(Boolean)
    totalIncludesTax = Column(Integer)
    totalTax = Column(DECIMAL(28, 9))
    subTotal = Column(DECIMAL(28, 9))
    totalPrice = Column(DECIMAL(28, 9))
    typeId = Column(Integer, ForeignKey('sotype.id'))
    typeObj = relationship('SalesOrderType', backref='sotype', foreign_keys=[typeId]) # type: SalesOrderType
    url = Column(String(256))
    username = Column(String(100))
    vendorPO = Column(String(256))
    dateCalStart = Column(DateTime)
    dateCalEnd = Column(DateTime)


    @classmethod
    def all_open_orders(cls) -> List['SalesOrder']:
        """Returns a list of all open orders."""
        # SalesOrderStatus id <= 25 are open orders
        return session.query(SalesOrder).filter(SalesOrder.statusId <= 25).all()


class SalesOrderItem(Base):
    __tablename__ = 'soitem'

    id = Column(Integer, primary_key=True)
    adjustAmount = Column(DECIMAL(28, 9))
    adjustPercentage = Column(DECIMAL(28, 9))
    customerPartNum = Column(String(30))
    dateLastFulfillment = Column(DateTime)
    dateLastModified = Column(DateTime)
    dateScheduledFulfillment = Column(DateTime)
    description = Column(String(255))
    exchangeSOLineItem = Column(Integer)
    itemAdjustId = Column(Integer)
    markupCost = Column(DECIMAL(28, 9))
    mcTotalPrice = Column(DECIMAL(28, 9))
    note = Column(String(255))
    productId = Column(Integer, ForeignKey('product.id'))
    productObj = relationship('Product', backref='product', foreign_keys=[productId]) # type: Product
    productNum = Column(String(30))
    qtyFulfilled = Column(DECIMAL(28, 9))
    qtyOrdered = Column(DECIMAL(28, 9))
    qtyPicked = Column(DECIMAL(28, 9))
    qtyToFulfill = Column(DECIMAL(28, 9))
    revLevel = Column(String(15))
    showItemFlag = Column(Boolean)
    soId = Column(Integer, ForeignKey('so.id'))
    soObj = relationship('SalesOrder', backref='so') # type: SalesOrder
    soLineItem = Column(Integer)
    statusId = Column(Integer, ForeignKey('soitemstatus.id'))
    statusObj = relationship('SalesOrderItemStatus', backref='soitemstatus', foreign_keys=[statusId]) # type: SalesOrderItemStatus
    taxId = Column(Integer)
    taxRate = Column(DECIMAL(28, 9))
    taxableFlag = Column(Boolean)
    totalCost = Column(DECIMAL(28, 9))
    totalPrice = Column(DECIMAL(28, 9))
    typeId = Column(Integer, ForeignKey('soitemtype.id'))
    typeObj = relationship('SalesOrderItemType', backref='soitemtype', foreign_keys=[typeId]) # type: SalesOrderItemType
    unitPrice = Column(DECIMAL(28, 9))
    uomId = Column(Integer, ForeignKey('uom.id'))
    uomObj = relationship('Uom', backref='uom') # type: Uom


    @property
    def qtyLeftToFulfill(self):
        """Returns the quantity left to fulfill."""
        return self.qtyToFulfill - self.qtyFulfilled - self.qtyPicked