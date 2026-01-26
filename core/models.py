from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: list[str]
    language: list[str] = []

class Work(BaseModel):
    work_id: str
    title: str
    authors: list[str] = []
    first_publish_year: int | None = None
    description: str | None = None

class Edition(BaseModel):
    work_id: str
    isbn_13: list[str] = []
    #isbn_10: str | None
    language: list[str] = []
    publishers: list[str] = []
    publish_date: str | None
class Language(BaseModel):
    key: str
    en_name: str | None
    es_name: str | None