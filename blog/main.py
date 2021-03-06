from fastapi import FastAPI
from sqlalchemy.orm.session import Session
from . import schemas
from . import models
from pydantic import BaseModel
from .database import engine,SessionLocal

app=FastAPI()


models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
       db.close()

@app.post('/blog')

def create(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,bode=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

