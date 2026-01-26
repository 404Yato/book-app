import json
import core.models as Models
import utils.save_files as SF
from pathlib import Path

def _read_language_file(file: Path):
    with file.open("r", encoding="utf-8") as f:
            return [Models.Language(**x) for x in json.load(f)]

def load_language() -> list['Models.Language']:
    FILE = Path("data/languages.json")
    if FILE.exists():
        print("Archivo de idiomas encontrado. Leyendo...")
        return _read_language_file(FILE)
    
    print("Archivo de idiomas no encontrado. Creando...")
    SF.save_languages_from_api()

    try:
        return _read_language_file(FILE)
    except (FileNotFoundError, json.JSONDecodeError):
        return []