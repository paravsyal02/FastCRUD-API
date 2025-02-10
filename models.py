# Import statements
from sqlalchemy import Column, Integer, String
from database import Base

# Class Definition
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer)