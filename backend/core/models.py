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

class Language(BaseModel):
    key: str
    en_name: str | None
    es_name: str | None

    @staticmethod
    def build_index(languages: list["Language"]) -> dict[str, "Language"]: #Construye un diccionario en base a una lista de idiomas (Clase) con estructura key : Language(Class)
        return {lang.key: lang for lang in languages}
    
class Edition(BaseModel):
    work_id: str
    isbn_13: list[str] = []
    #isbn_10: str | None
    language: list[str] = []
    publishers: list[str] = []
    publish_date: str | None

    def resolve_languages(self, languages: list[Language]) -> list[str]:
        index = Language.build_index(languages)

        return [
            f"{index[key].es_name} / {index[key].en_name}"
            for key in self.language
            if key in index
        ]