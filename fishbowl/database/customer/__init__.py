"""Contains all classes related to Customers."""


import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL, Boolean
from sqlalchemy.orm import relationship, backref
from fishbowl.database import Base
from fishbowl.database.account import Account
from fishbowl.database.user import User



class Customer(Base):
    """Represents a customer."""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    accountId = Column(Integer, ForeignKey('account.id'))
    accountObj = relationship('Account', backref=backref('customerObj', lazy=True)) # type: Account
    activeFlag = Column(Integer, default=True)
    # TODO: Add carrier service relationship.
    # carrierServiceId = Column(Integer, ForeignKey('carrierservice.id'))
    # carrierServiceObj = relationship('CarrierService', backref=backref('customerObj_carrierService', lazy=True)) # type: CarrierService
    creditLimit = Column(DECIMAL(28, 9), default=0.00)
    # TODO: Add currency relationship.
    # currencyId = Column(Integer, ForeignKey('currency.id'))
    # currencyObj = relationship('Currency', backref=backref('customerObj_currency', lazy=True)) # type: Currency
    currencyRate = Column(DECIMAL(28, 9), default=0.00)
    dateCreated = Column(DateTime, default=datetime.datetime.now())
    dateLastModified = Column(DateTime, default=datetime.datetime.now())
    # TODO: Add default carrier relationship.
    # defaultCarrierId = Column(Integer, ForeignKey('carrier.id'))
    # defaultCarrierObj = relationship('Carrier', backref=backref('customerObj_defaultCarrier', lazy=True)) # type: Carrier
    # TODO: Add default payment terms relationship.
    # defaultPaymentTermsId = Column(Integer, ForeignKey('paymentterms.id'))
    # defaultPaymentTermsObj = relationship('PaymentTerms', backref=backref('customerObj_defaultPaymentTerms', lazy=True)) # type: PaymentTerms
    defaultSalesmanId = Column(Integer, ForeignKey('sysuser.id'))
    defaultSalesmanObj = relationship('User', backref=backref('customerObj_defaultSalesman', lazy=True), foreign_keys=[defaultSalesmanId]) # type: User
    # TODO: Add default ship terms relationship.
    # defaultShipTermsId = Column(Integer, ForeignKey('shippingterms.id'))
    # defaultShipTermsObj = relationship('ShippingTerms', backref=backref('customerObj_defaultShipTerms', lazy=True)) # type: ShippingTerms
    jobDepth = Column(Integer)
    lastChangedUser = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    note = Column(String(255))
    number = Column(String(255), unique=True)
    # TODO: Add status relationship.
    # statusId = Column(Integer, ForeignKey('customerstatus.id'))
    # statusObj = relationship('CustomerStatus', backref=backref('customerObj_status', lazy=True)) # type: CustomerStatus
    sysUserId = Column(Integer, ForeignKey('sysuser.id'))
    sysUserObj = relationship('User', backref=backref('customerObj_sysUser', lazy=True), foreign_keys=[sysUserId]) # type: User
    taxExempt = Column(Boolean, default=False)
    taxExemptNumber = Column(String(255))
    # TODO: Add tax rate relationship.
    # taxRateId = Column(Integer, ForeignKey('taxrate.id'))
    # taxRateObj = relationship('TaxRate', backref=backref('customerObj_taxRate', lazy=True)) # type: TaxRate
    toBeEmailed = Column(Boolean, default=False)
    toBePrinted = Column(Boolean, default=False)
    url = Column(String(255))
    # TODO: Add issuable status relationship.
    # issuableStatusId = Column(Integer, ForeignKey('issuestatus.id'))
    # issuableStatusObj = relationship('IssueStatus', backref=backref('customerObj_issuableStatus', lazy=True)) # type: IssueStatus
    defaultPriorityId = Column(Integer)