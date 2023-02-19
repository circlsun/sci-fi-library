
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from livereload import Server
from more_itertools import chunked


def rebuild():
    with open("json/books_description.json", "r") as file:
        books = json.load(file)
    books_inline = list(chunked(books, 2))

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(books_inline=books_inline)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
        print("Site rebuilt")


rebuild()
server = Server()
server.watch('template.html', rebuild)
server.serve(root='.')
