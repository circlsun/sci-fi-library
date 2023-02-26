import json
import os
from math import ceil

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def rebuild():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    with open('json/books_description.json', 'r') as file:
        books_description = json.load(file)

    columns = 2
    books_per_page = 10
    pagination_size = ceil((len(books_description) / columns) / books_per_page)

    book_cards_in_row = list(chunked(books_description, columns))
    book_cards_in_pages = list(chunked(book_cards_in_row, pagination_size))
    pages_amount = len(book_cards_in_pages)

    template = env.get_template('template.html')
    for book_index, books_in_page in enumerate(book_cards_in_pages, start=1):
        rendered_page = template.render(
            books_in_page=books_in_page,
            pages_amount=pages_amount,
            current_page=book_index
        )

        with open(f'pages/index{book_index}.html', 'w', encoding='utf8') as file:
            file.write(rendered_page)

def main():
    os.makedirs('pages', exist_ok=True)
    rebuild()
    server = Server()
    server.watch('template.html', rebuild)
    server.serve(root='.')

if __name__ == '__main__':
    main()
