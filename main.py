import sources as Sources
import utils as Utils
# books = Sources.open_library.search_works("Un mundo feliz", "Aldous Huxley")

# for b in books:
#     print(f"ID de la obra: {b.work_id}")
#     print(f"Título: {b.title}")
#     print(f"Autor/es: {','.join(b.authors)}")
#     print(f"Año de primera publicación: {b.first_publish_year}")
#     print(f"Descripción: {b.description}") if b.description else None
#     print("-" * 40)

#     editions = Sources.open_library.search_editions(b.work_id)
#     print("Ediciones:")
#     for e in editions:
#         print(f"  ISBN-13: {','.join(e.isbn_13)}") if e.isbn_13 else None
#         print(f"  Idioma/s: {','.join(e.language)}") if e.language else None
#         print(f"  Editorial/es: {','.join(e.publishers)}") if e.publishers else None
#         print(f"  Fecha de publicación: {e.publish_date}") if e.publish_date else None
#         print("  " + "-" * 20)

# languages = Sources.open_library.get_languages()

# for l in languages:
#     print(f'Key: {l.key}')
#     print(f'Nombre: {l.en_name}')
#     print(f'Nombre Español: {l.es_name}')
#     print('-' * 20)

languages = Utils.load_files.load_language()
for l in languages:
    print(f'Key: {l.key}')
    print(f'Nombre: {l.en_name}')
    print(f'Nombre Español: {l.es_name}')
    print('-' * 20)