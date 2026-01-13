import requests
import time
import core.models as Models
import json

def search_books(query: str, author: str = None, mode: str = "everything") -> list['Models.Book']:
    API_URL = "https://openlibrary.org/search.json"
    params={
        'q': query,
        'author': author,
        'mode': mode}
    response = requests.get(API_URL, params=params)
    data = response.json()
    print(response.url)
    books = []
    for i in data.get("docs", []):
        book = Models.Book(title = i["title"], author = i.get("author_name", ["Uknown Author"]), language = i.get("language", ["Uknown Language"]))
        books.append(book)
    return books