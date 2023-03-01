from sqlalchemy import Column, Integer, String
import hashlib
from settings import PASSWORD_SALT
from database import Base
from fastapi import HTTPException


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)
    money = Column(Integer, default=100)

    def check_password(self, passed_password):
        hashed_passed_password = hashlib.sha256((passed_password + PASSWORD_SALT).encode()).hexdigest().lower()
        if self.password == hashed_passed_password:
            return self
        else:
            raise HTTPException(status_code=400, detail="Wrong password")
