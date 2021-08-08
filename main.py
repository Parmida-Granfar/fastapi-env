from typing import Optional
from fastapi import FastAPI 
from pydantic import BaseModel

#import uvicorn 
app=FastAPI()   #instance

@app.get('/blog')     #decorate.This is called path operation decorater
def index(limit=10,published:bool=True,sort:Optional[str]=None): 
    if published:    #function
        return {'data':f'{limit} published blogs from db'} #this is called path operation
    else:
        return {'data':f'{limit} unpublished blogs from db'}
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')   #when you need dynamic routing you use curly braces
def show(id:int):     #function
    return {'data':id}



@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body:str
    published_at:Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return{'data':f'Blog is created with title as {request.title}'}

#if __name__=='__main__':
   #uvicorn.run(app,host='127.0.0.1',port='9000')

