from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()

users_bd = {}

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sign_up", response_model=schemas.UserCreated)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)


@app.post("/get_money", response_model=schemas.User)
def get_user_money(user: schemas.UserCreate, db: Session = Depends(get_db)):
    money_amount = crud.sign_in(db, name=user.name, password=user.password)
    if not money_amount:
        raise HTTPException(status_code=400, detail='There is no such user')
    return money_amount


@app.get("/users/user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    info = crud.get_user_by_id(db, user_id)
    if not info:
        raise HTTPException(status_code=400, detail="There is no user with such ID")
    print(type(info))
    return info


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
