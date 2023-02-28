from pydantic import BaseModel
import hashlib
from settings import PASSWORD_SALT


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str

    def hash_password(self):
        # password = self.password + '1'
        password = hashlib.sha256((self.password + PASSWORD_SALT).encode()).hexdigest().lower()
        return password


class User(UserBase):
    id: int
    money: int

    class Config:
        orm_mode = True


class UserCreated(User, UserCreate):
    pass
