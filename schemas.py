from pydantic import BaseModel
import hashlib
from settings import PASSWORD_SALT


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str

    def hash_password(self):
        password = hashlib.sha256((self.password + PASSWORD_SALT).encode()).hexdigest().lower()
        return password


class UserMoney(UserBase):
    money: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInfo(User, UserMoney):
    pass


class UserCreated(User, UserMoney, UserCreate):
    pass
