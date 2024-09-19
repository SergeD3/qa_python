from helpers import fill_books_genre
from db_data import books_genres

import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self, book):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(book.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_two_identical_books_added_one(self, book):
        book.add_new_book('Война и мир')
        book.add_new_book('Война и мир')

        assert len(book.books_genre) == 1

    def test_add_new_book_book_name_more_than41_digits_get_empty_dict(self, book):
        book.add_new_book('Агата Кристи: Убийство в Восточном экспрессе')

        assert book.books_genre == {}

    def test_set_book_genre_set_book_genre(self, book):
        name = ['Сборник анекдотов про Чапаева и Петьку', 'Комедии']
        book.add_new_book(name[0])
        book.set_book_genre(name[0], name[1])

        assert book.get_book_genre(name[0]) == name[1]

    @pytest.mark.parametrize('name, genre', books_genres)
    def test_set_book_genre_set_unknown_book_empty_books_genre(self, book, name, genre):
        book.set_book_genre(name, genre)

        assert len(book.books_genre) == 0

    @pytest.mark.parametrize('name, genre', books_genres)
    def test_get_book_genre_get_genre_added_book(self, book, name, genre):
        book.add_new_book(name)
        book.set_book_genre(name, genre)

        assert book.get_book_genre(name) == genre

    def test_get_book_genre_set_unknown_book_get_none(self, book):
        assert book.get_book_genre('Страна чудес без тормозов и Конец Света') is None

    def test_get_books_with_specific_genre_add_books_get_comedy_books(self, book):
        name = ['Сборник анекдотов про Чапаева и Петьку', 'Комедии']
        book.add_new_book(name[0])
        book.set_book_genre(name[0], name[1])
        comedy_books = book.get_books_with_specific_genre(name[1])

        assert name[0] in comedy_books

    def test_get_books_for_children_get_books_for_children(self, book):
        fill_books_genre(book)

        assert len(book.get_books_for_children()) == 3

    def test_get_books_with_specific_genre_genre_not_in_list_get_empty_list(self, book):
        assert book.get_books_with_specific_genre('Sci-fi') == []

    def test_add_book_in_favorites_add_one_book_get_one_item_list(self, book):
        book_name = 'Оно'
        book.add_new_book(book_name)
        book.add_book_in_favorites(book_name)

        assert book_name in book.favorites

    def test_delete_book_from_favorites_delete_book_from_favorites(self, book):
        book_name = 'Оно'
        fill_books_genre(book)
        book.add_book_in_favorites(book_name)
        book.delete_book_from_favorites(book_name)

        assert book_name not in book.favorites
