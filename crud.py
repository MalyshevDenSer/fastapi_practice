from sqlalchemy.orm import Session

import models
from schemas import UserCreate


def sign_in(db: Session, name: str, password: str):
    user = db.query(models.User).filter(models.User.name == name).first()
    if user:
        return user.check_password(password)
    return False


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = models.User(name=user.name, password=user.hash_password())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_user.password = user.password
    return db_user
