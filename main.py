from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, sessionmaker
from orm import User,Base
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_session():
    session=SessionLocal()
    try:
        yield session
    finally:
        session.close()


app = FastAPI()

@app.get('/users/')
def get_users(session: Session = Depends(get_session)):
    return session.query(User).all()