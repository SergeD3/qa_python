# qa_python

1. test_add_new_book_add_two_identical_books_added_one - проверяет, что при добавлении двух одинаковых книг добавляется только одна.
2. test_add_new_book_book_name_more_than41_digits_get_empty_dict - проверяет, что если название книги длинее чем 41 символ, то книга не добавляется в словарь.
3. test_set_book_genre_set_book_genre - проверяет, что метод метод set_book_genre устанавливает добавленной книге переданный жанр.
4. test_set_book_genre_set_unknown_book_empty_books_genre - проверяет, что если в методе не выполняется условие, то books_genre остаётся пустым.
5. test_get_book_genre_get_genre_added_book - проверяет, что метод возвращает жанр добавленной книги.
6. test_get_book_genre_set_unknown_book_get_none - проверяет, что метод возвращает None если книги нет в словаре books_genre.
7. test_get_books_with_specific_genre_add_books_get_comedy_books - проверяет, что метод возвращает список книг в жанре комедия.
8. test_get_books_with_specific_genre_genre_not_in_list_get_empty_list - проверяет, что метод возвращает пустой список, когда жанра нет в списке self.genre.
9. test_get_books_for_children_get_books_for_children - проверяет, что метод возвращает список книг которые подходят под условие метода.
10. test_add_book_in_favorites_add_one_book_get_one_item_list - проверяет, что метод добавляет переданную книгу в список favorites.
11. test_delete_book_from_favorites_delete_book_from_favorites - проверяет, что метод удаляет переданную книгу из списка favorites.

