from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, create_engine
from datetime import datetime

engine = create_engine("sqlite:///blogs.db", echo=True)
Session = sessionmaker(bind=engine)


def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()



class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    created_at = Column(DateTime, default=datetime.now())

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    image = Column(Text)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True, index=True, nullable=False)
    email = Column(Text, unique=True, index=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())