import json
import sources as Sources

def save_languages_from_api():
    languages = Sources.open_library.get_languages()

    data = [lang.model_dump() for lang in languages]

    with open("data/languages.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)