from fastapi import FastAPI, Depends
from models import Post, User, Category, get_db
from schemas import PostSchema, CategorySchema, UserSchema
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins = ["*"], allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get('/posts')
def post(session = Depends(get_db)):
    posts = session.query(Post).all()
    return posts

@app.post('/posts')
def add_post(post: PostSchema, session = Depends(get_db)):
    new_post = Post(**post.model_dump())
    session.add(new_post) 
    session.commit()
    return {"message": "post added successfully"}

@app.get('/users')
def user(session = Depends(get_db)):
    users = session.query(User).all()
    return users

# @app.post('/users')
# def add_user(post: UserSchema, session = Depends(get_db)):
#     new_user = User(**post.model_dump())
#     session.add(new_user)
#     session.commit()
#     return {"message": "User added successfully"}



