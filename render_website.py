
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from livereload import Server
from more_itertools import chunked


def rebuild():
    with open("json/books_description.json", "r") as file:
        books = json.load(file)
    columns = 2
    books_in_row = list(chunked(books, columns))

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(books_in_row=books_in_row)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
        print("Site rebuilt")


rebuild()
server = Server()
server.watch('template.html', rebuild)
server.serve(root='.')
