from sqlalchemy import Column, Integer, String

from .processor import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    detailed_occupation = Column(String)
    password = Column(String)
