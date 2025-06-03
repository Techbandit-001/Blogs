from pydantic import BaseModel, HttpUrl
from typing import Literal

class PostSchema(BaseModel):
    title: str
    content: str
    category: Literal["tech", "faith", "lifestyle", "other"]
    image: HttpUrl  # ✅ not just str

class CategorySchema(BaseModel):
    
    name: str
    
class UserSchema(BaseModel):
    username: str
    email: str
    harshed_password: str


   