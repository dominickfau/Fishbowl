"""Contains all classes relateing to Users."""

import base64
import hashlib
from sqlalchemy import Column, Integer, String, Boolean
from fishbowl.database import Base, session



class User(Base):
    """Represents a user."""
    __tablename__ = 'sysuser'

    id = Column(Integer, primary_key=True)
    activeFlag = Column(Boolean, nullable=False, default=True)
    email = Column(String(255), unique=True)
    firstName = Column(String(15), nullable=False)
    initials = Column(String(5), nullable=False)
    lastName = Column(String(15), nullable=False)
    phone = Column(String(255))
    userName = Column(String(100), unique=True, nullable=False)
    userPwd = Column(String(30), nullable=False)

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default Users."""
        default_user = cls(id=1, userName='admin', password='admin', firstName='Administrator', lastName='Administrator', initials='AD')
        session.add(default_user)
        session.commit()

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes password string using this method, Base64.encode(MD5.hash(password))

        Args:
            password (string): Plain text string of the password to hash.

        Returns:
            string: The hashed password string.
        """
        password = password.strip()
        return base64.b64encode(hashlib.md5(password.encode()).digest()).decode('utf-8')

    @property
    def password(self):
        """Prevent password from being accessed."""
        raise AttributeError('password is not a readable attribute!')
    
    @property
    def full_name(self) -> str:
        """Return the full name of the user. In the following format: firstName - lastName"""
        return f"{self.firstName} - {self.lastName}"

    @password.setter
    def password(self, password: str):
        """Hash password on the fly. This allows the plan text password to be used when creating a User instance."""
        self.userPwd = User.hash_password(password)
    
    def verify_password(self, password: str) -> bool:
        """Check if hashed password matches the one provided."""
        return self.userPwd == User.hash_password(password)
