import json
from random import randint
from random import uniform
from faker import Faker
from conf import MODEL


pk = 1


def get_title():
    with open("books.txt", "r") as file:
        titles = file.read().split("\n")
        return titles[randint(0, len(titles) - 1)]


def get_year():
    return randint(0, 2023)


def get_pages():
    return randint(0, 1000)


def get_isbn():
    fake = Faker()
    return fake.isbn13()


def get_rating():
    return round(uniform(0, 5.0), 1)


def get_price():
    return round(uniform(0, 1000), 1)


def get_author():
    fake = Faker()
    Faker.seed()
    return [fake.name() for authors in range(randint(1, 3))]


def get_pk():
    global pk
    old_state = pk
    pk += 1
    return old_state


def generate_books(count, init_pk=None):
    global pk
    if init_pk is not None:
        pk = init_pk
    books = []
    for i in range(count):
        book = {"model": MODEL, "pk": get_pk()}
        fields = {}
        fields.update({"title": get_title()})
        fields.update({"year": get_year()})
        fields.update({"pages": get_pages()})
        fields.update({"isbn13": get_isbn()})
        fields.update({"rating": get_rating()})
        fields.update({"price": get_price()})
        fields.update({"author": get_author()})
        book.update({"fields": fields})
        books.append(book)
    return books


def books():
    books = generate_books(100)
    with open("result.json", "w") as json_file:
        json_string = json.dumps(books, indent=3)
        json_file.write(json_string)


if __name__ == '__main__':
    books()
