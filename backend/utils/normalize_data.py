import core.models as Models
import utils.load_files as LD

def normalize_editions(editions : list["Models.Editions"]): #Creada principalmente para transformar el código de idioma en el nombre del idioma de la edición
    normalized_editions = []
    languages = LD.load_language()
    for e in editions:
        edition = Models.Edition(
            work_id = e.work_id,
            isbn_13 = e.isbn_13,
            language = e.resolve_languages(languages),
            publishers = e.publishers,
            publish_date = e.publish_date
        )
        normalized_editions.append(edition)
    return normalized_editions