from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: list[str]
    language: list[str] = []