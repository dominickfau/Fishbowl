from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from fishbowl.database import Base, engine
from fishbowl.database.baseclass import BaseType


class AccountType(BaseType):
    """Represents Account Types."""
    __tablename__ = 'accounttype'

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default AccountTypes."""
        return [
            cls(id=10, name='Retail'),
            cls(id=20, name='Wholesale'),
            cls(id=30, name='Internet')
        ]

class Account(Base):
    """Represents an Account."""
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    typeId = Column(Integer, ForeignKey('accounttype.id'))
    typeObj = relationship('AccountType', backref='accountType') # type: AccountType