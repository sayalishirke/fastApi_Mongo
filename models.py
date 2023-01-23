from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    password: str

class Blog(BaseModel):
    id: int
    title: str
    body : str