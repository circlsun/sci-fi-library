
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from livereload import Server


def rebuild():
    with open("json/books_description.json", "r") as f:
        books_descriptions_json = f.read()
    books = json.loads(books_descriptions_json)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(books=books)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
        print("Site rebuilt")


rebuild()
server = Server()
server.watch('template.html', rebuild)
server.serve(root='.')
