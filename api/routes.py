from fastapi import APIRouter, Query, HTTPException
import utils.load_files as LF
import sources as Sources

router = APIRouter(prefix="/api")

@router.get("/languages")
def get_languages():
    return LF.load_language()

@router.get("/books/search")
def search_books(book_name : str = Query(default=None), author : str = Query(default=None)):
    if not book_name and not author:
        raise HTTPException(status_code=400, detail="Se debe entregar al menos un autor o nombre del libro")
    
    return Sources.open_library.search_works(book_name, author)