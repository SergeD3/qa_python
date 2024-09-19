from db_data import books_genres


def fill_books_genre(book):
    for b in range(len(books_genres)):
        book.add_new_book(books_genres[b][0])
        book.set_book_genre(books_genres[b][0], books_genres[b][1])
