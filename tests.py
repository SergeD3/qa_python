from main import BooksCollector

import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    books_genres = [
        ['Дюна', 'Фантастика'],
        ['Оно', 'Ужасы'],
        ['Шерлок Холмс', 'Детективы'],
        ['Алиса в Стране чудес', 'Мультфильмы'],
        ['Три мушкетера', 'Комедии'],
        ['Гарри Поттер и философский камень', 'Фантастика'],
        ['Дракула', 'Ужасы'],
        ['Красавица и чудовище', 'Мультфильмы'],
        ['Дон Кихот', 'Комедии'],
    ]

    def fill_books_genre(self):
        for b in range(len(self.books_genres)):
            self.book.add_new_book(self.books_genres[b][0])
            self.book.set_book_genre(self.books_genres[b][0], self.books_genres[b][1])

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    @pytest.fixture(autouse=True)
    def book(self):
        self.book = BooksCollector()

        return self.book

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_two_identical_books_added_one(self):
        self.book.add_new_book('Война и мир')
        self.book.add_new_book('Война и мир')

        assert len(self.book.books_genre) == 1

    def test_add_new_book_book_name_more_than41_digits_get_empty_dict(self):
        self.book.add_new_book('Агата Кристи: Убийство в Восточном экспрессе')

        assert self.book.books_genre == {}

    @pytest.mark.parametrize('name, genre', books_genres)
    def test_set_book_genre_set_book_genre(self, name, genre):
        self.book.add_new_book(name)
        self.book.set_book_genre(name, genre)

        assert self.book.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', books_genres)
    def test_set_book_genre_set_unknown_book_empty_books_genre(self, name, genre):
        self.book.set_book_genre(name, genre)

        assert len(self.book.books_genre) == 0

    @pytest.mark.parametrize('name, genre', books_genres)
    def test_get_book_genre_get_genre_added_book(self, name, genre):
        self.book.add_new_book(name)
        self.book.set_book_genre(name, genre)

        assert self.book.get_book_genre(name) == genre

    def test_get_book_genre_set_unknown_book_get_none(self):
        assert self.book.get_book_genre('Страна чудес без тормозов и Конец Света') is None

    def test_get_books_with_specific_genre_add_books_get_comedy_books(self):
        self.fill_books_genre()

        assert len(self.book.get_books_with_specific_genre("Комедии")) == 2

    def test_get_books_with_specific_genre_genre_not_in_list_get_empty_list(self):
        assert self.book.get_books_with_specific_genre('Sci-fi') == []

    def test_get_books_for_children_get_books_for_children(self):
        self.fill_books_genre()

        assert len(self.book.get_books_for_children()) == 6

    def test_add_book_in_favorites_add_one_book_get_one_item_list(self):
        book_name = 'Оно'
        self.fill_books_genre()
        self.book.add_book_in_favorites(book_name)

        assert book_name in self.book.favorites

    def test_delete_book_from_favorites_delete_book_from_favorites(self):
        book_name = 'Оно'
        self.fill_books_genre()
        self.book.add_book_in_favorites(book_name)
        self.book.delete_book_from_favorites(book_name)

        assert book_name not in self.book.favorites

    def test_get_list_of_favorites_books_get_list_of_favorites_books(self):
        book_name = ['Оно', 'Дюна', 'Дракула']
        self.fill_books_genre()

        for n in book_name:
            self.book.add_book_in_favorites(n)

        assert book_name == self.book.get_list_of_favorites_books()
