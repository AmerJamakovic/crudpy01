from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, sessionmaker
from models import User, Base
from db import get_session, init_db
import hashlib
from schemas import UserReadSimple, UserRead
from typing import List

app = FastAPI()


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/users/", response_model=List[UserRead])
def get_users(session: Session = Depends(get_session)):
    users = session.query(User).all()
    return users
