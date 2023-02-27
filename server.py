from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# class UserData(BaseModel):
#     id: int
#     name: str
#     surname: str
#     detailed_occupation: Union[str, None]
#     password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

users_bd = {}


@app.post("/sign_up")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
    # user_id = max(users_bd, default=0) + 1
    # users_bd[user_id] = {
    #     'name': data.name,
    #     'surname': data.surname,
    #     'detailed_occupation': data.detailed_occupation,
    #     'password': data.password
    # }
    # return test_param


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# @app.get("/give_all_bd")
# def give_all_bd():
#     return users_bd
