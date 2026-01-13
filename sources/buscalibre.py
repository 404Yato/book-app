import requests
from bs4 import BeautifulSoup
import time
import re
from typing import Iterator, Optional
import logging
import core.models as Models

base_url = "https://www.buscalibre.com"
search_url = f"{base_url}/libros/search/"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "es-CL,es;q=0.9",
    "Referer": "https://www.buscalibre.cl/",
    "Connection": "keep-alive",
}

request_delay = 3  # seconds

def search_books(query: str, sort: str = "42_price-asc", max_pages: int = 1) -> Iterator['Models.Book']:
    session = requests.Session()
    session.headers.update(headers)
    
    for page in range(1, max_pages + 1):
        params = {
            'q': query,
            'sort': sort,
            'page': page
        }
        home_page = session.get(base_url)
        if home_page.status_code != 200:
            logging.warning(f"Failed to retrieve home page: {home_page.status_code}")
            break
        time.sleep(request_delay)
        response = session.get(search_url, params=params)
        if response.status_code != 200:
            logging.warning(f"Failed to retrieve page {page}: {response.status_code}")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        book_items = soup.select('div.box-producto')
        
        if not book_items:
            break
        
        for item in book_items:
            #title_elem = item.select_one('.product-title a')
            #author_elem = item.select_one('.product-author')
            #isbn_elem = item.select_one('.data-isbn')
            isbn_elem = item["data-isbn"]
            price_elem = int(item["data-precio"])
            link_elem = item.select_one("a")["href"]
            title_elem = item.select_one("h3.nombre").get_text(strip=True)
            author_elem = item.select_one("div.autor").get_text(strip=True)

            if title_elem and author_elem and isbn_elem:
                title = title_elem
                author = author_elem
                
                yield Models.Book(title=title, author=[author])
        
        
        time.sleep(request_delay)