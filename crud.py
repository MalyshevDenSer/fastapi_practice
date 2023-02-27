from sqlalchemy.orm import Session

import models
from schemas import UserCreate


def sign_in(db: Session, name: str, password: str):
    user = db.query(models.User).filter(models.User.name == name).first()
    if user:
        if user.hashed_password == password:
            return db.query(models.User).filter(models.User.name == name).first().money
        else:
            return 'Wrong password'
    else:
        return 'This user does not exist'


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
