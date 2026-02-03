from fastapi import APIRouter, Query, HTTPException
import utils.load_files as LF
import utils.normalize_data as ND
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

@router.get("/editions/{work_id:path}")  #Se usa path debido a que work_id contiene "/" en su texto, de esta forma se evita un code 404.
def search_editions(work_id : str):
    return ND.normalize_editions(Sources.open_library.search_editions(work_id))