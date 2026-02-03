import requests
import time
import core.models as Models
import json

def search_works(query: str, author: str = None, mode: str = "everything") -> list['Models.Work']:
    API_BASE_URL = "https://openlibrary.org"
    API_SEARCH_URL = f"{API_BASE_URL}/search.json"
    params={
        'q': query,
        'author': author,
        'mode': mode}
    response = requests.get(API_SEARCH_URL, params=params)
    data = response.json()
    print(response.url)
    books = []
    for i in data.get("docs", []):
        #book = Models.Book(title = i["title"], author = i.get("author_name", ["Uknown Author"]), language = i.get("language", ["Uknown Language"]))
        # API_WORK_URL = f"{API_BASE_URL}{i['key']}.json"
        # response_work = requests.get(API_WORK_URL)
        # data_work = response_work.json()
        # raw_description = data_work.get("description")
        # description = (
        #     raw_description.get("value")
        #     if isinstance(raw_description, dict)
        #     else raw_description
        # )
        book = Models.Work(work_id = i["key"][1:] if i["key"][1:] else i["key"],
                            title = i["title"],
                            authors = i.get("author_name", ["Uknown Author"]),
                            first_publish_year = i.get("first_publish_year", None))
        books.append(book)
    return books

def search_editions(work_id: str) -> list['Models.Edition']:
    API_BASE_URL = "https://openlibrary.org"
    API_EDITIONS_URL = f"{API_BASE_URL}/{work_id}/editions.json"
    response = requests.get(API_EDITIONS_URL)
    data = response.json()
    editions = []
    for i in data.get("entries", []):
        languages = []
        for lang in i.get("languages", []):
            key = lang.get("key")
            if key:
                languages.append(key)
        edition = Models.Edition(
            work_id = work_id,
            isbn_13 = i.get("isbn_13", ['Not Found']),
            #isbn_10 = i.get("isbn_10", [None])[0],
            language = languages,
            publishers = i.get("publishers", ['Not Found']),
            publish_date = i.get("publish_date", None),
        )
        editions.append(edition)
    return editions

def get_languages() -> list['Models.Language']:
    API_BASE_URL = "https://openlibrary.org"
    API_LANGUAGES_URL = f"{API_BASE_URL}/languages.json"
    response = requests.get(API_LANGUAGES_URL)
    data = response.json()
    languages = []
    for d in data:
        lang_resp = requests.get(API_BASE_URL + d.get('key', None) + '.json')
        lang_data = lang_resp.json()
        language = Models.Language(
            key = d.get('key', None),
            en_name = lang_data.get('name', None),
            es_name = lang_data.get('name_translated', {}).get('es')[0].capitalize()
        )
        languages.append(language)
    return languages
