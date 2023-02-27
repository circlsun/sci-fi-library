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

    with open('json/books_description.json', 'r', encoding="utf8") as file:
        books_description = json.load(file)

    columns = 2
    book_cards_per_page = 10

    book_cards_in_row = list(chunked(books_description, columns))
    book_cards_in_pages = list(chunked(book_cards_in_row, book_cards_per_page))
    pages_amount = len(book_cards_in_pages)

    template = env.get_template('template.html')
    for page_index, page in enumerate(book_cards_in_pages, start=1):
        rendered_page = template.render(
            books_in_page=page,
            pages_amount=pages_amount,
            current_page=page_index
        )

        with open(f'pages/index{page_index}.html', 'w', encoding='utf8') as file:
            file.write(rendered_page)


def main():
    os.makedirs('pages', exist_ok=True)
    rebuild()
    server = Server()
    server.watch('template.html', rebuild)
    server.serve(root='.')


if __name__ == '__main__':
    main()
