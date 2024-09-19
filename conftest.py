from main import BooksCollector

import pytest


@pytest.fixture(autouse=True)
def book():
    book = BooksCollector()

    return book
