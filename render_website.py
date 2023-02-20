
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import os
from livereload import Server
from more_itertools import chunked

os.makedirs('pages', exist_ok=True)


def rebuild():
    with open("json/books_description.json", "r") as file:
        books = json.load(file)
    columns = 2
    pages = 5
    books_in_row = list(chunked(books, columns))
    books_in_pages = list(chunked(books_in_row, pages))

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    for num, books_in_page in enumerate(books_in_pages):
        rendered_page = template.render(books_in_page=books_in_page)

        with open(f'pages/index{num}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)
            print("Site rebuilt")


rebuild()
server = Server()
server.watch('template.html', rebuild)
server.serve(root='.')
