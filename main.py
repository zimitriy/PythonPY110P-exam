from faker import Factory
from faker import Faker
fake1 = Factory.create()
from conf import MODEL
import random

title = list(open('books.txt'))

def books():
    fields = {
        'title': random.choice(title).rstrip(),
        'year': random.randrange(1900, 2023),
        'pages': random.randrange(1000),
        'isbn13': fake1.isbn13(),
        'rating': round(random.uniform(0.0, 5.0), 1),
        'price': round(random.uniform(0, 1000), 2),
        'author': fake1.name()
    }
    # return {key: value for key, value in fields.items()}
    for key, value in fields.items():
        print(f'{key}-{value}')


print(books())
