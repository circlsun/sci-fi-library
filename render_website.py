
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import os
from math import ceil
from livereload import Server
from more_itertools import chunked

os.makedirs('pages', exist_ok=True)


def rebuild():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    with open("json/books_description.json", "r") as file:
        books = json.load(file)

    columns = 2
    books_per_page = 10
    pages = ceil((len(books) / columns) / books_per_page)

    books_in_row = list(chunked(books, columns))
    books_in_pages = list(chunked(books_in_row, pages))
    total_pages = len(books_in_pages)

    template = env.get_template('template.html')
    for num, books_in_page in enumerate(books_in_pages):
        rendered_page = template.render(
            books_in_page=books_in_page,
            total_pages=total_pages,
            current_page=num + 1
        )

        with open(f'pages/index{num + 1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


rebuild()
server = Server()
server.watch('template.html', rebuild)
server.serve(root='.')
