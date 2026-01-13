import sources as Sources

books = Sources.open_library.search_books("", "Stephen King")

for b in books:
    print(f"Título: {b.title}")
    print(f"Autor/es: {','.join(b.author)}")
    print(f"Idioma: {','.join(b.language)}")