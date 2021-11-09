"""
@author: Yogeshwar
@Goal: To implement custom data type Book
"""

import sys


class Book:
    """
    @constructor:   Accepts book title, book publisher, genre, number of pages,
                    edition, reprint, ISBN, and price from the client
    @class methods
    """
    def __init__(self, init_bk_title: str, init_bk_authors: list, init_bk_publisher: str,
                 init_bk_genre: str, init_bk_nr_pages: int, init_bk_nr_edition: int,
                 init_bk_nr_reprint: int, init_bk_isbn: str, init_bk_price: float):
        """Constructor procedure
        @init_bk_title: Title of the book : str
        @init_bk_authors: List of authors of the book : list of strings
        @init_bk_publisher: Publisher of the book : str
        @init_bk_genre: Genre of the book : str
        @init_bk_nr_pages: Number of pages in book : int
        @init_bk_nr_edition: Edition of the book: int
        @init_bk_nr_reprint: Reprint of the book: int
        @init_bk_isbn: ISBN of the book: str
        @init_bk_price: price of the book: int or float
        """
        if (type(init_bk_title) != str or # this is type checking
            type(init_bk_authors) != list or
            type(init_bk_publisher) != str or
            type(init_bk_genre) != str or
            type(init_bk_nr_pages) != int or
            type(init_bk_nr_edition) != int or
            type(init_bk_nr_reprint) != int or
            type(init_bk_isbn) != str or
            (type(init_bk_price) != int and type(init_bk_price) != float)
            ):
            print("Bad type for book constructor parameters")
            sys.exit(-1)
        self.bk_title = init_bk_title
        self.bk_authors = init_bk_authors
        self.bk_publisher = init_bk_publisher
        self.bk_genre = init_bk_genre
        self.bk_nr_pages = init_bk_nr_pages
        self.bk_nr_edition = init_bk_nr_edition
        self.bk_nr_reprint = init_bk_nr_reprint
        self.bk_isbn = init_bk_isbn
        self.bk_price = init_bk_price


B = Book("Introduction to Algorithms", ['Cormen', 'Leiserson', 'Rivest', 'Stein'],
         'MIT Press', 'Algorithms', 1292, 3, 1, "978-0-262-03384-8", 3500)

print("type(B):", type(B))

print("Printing Dictionary Inside Book object B:", B.__dict__)

