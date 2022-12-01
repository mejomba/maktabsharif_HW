from typing import List
from functools import reduce
from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salam(self):
        pass


class Librarian(Human):

    @staticmethod
    def search_book_by_id(identifier):
        result = []
        for shelve in Shelve.shelve_database.values():
            for book in shelve.books:
                if identifier == book.isbn:
                    res = f'{book.name} - {shelve.id} - {book.author.name} - {book.isbn}'
                    result.append(res)
        return result

    @staticmethod
    def search_book_by_name_or_id(writer_name_or_id):
        result = []
        for shelve in Shelve.shelve_database.values():
            for book in shelve.books:
                if book.author.name == writer_name_or_id or book.author.code == writer_name_or_id:
                    res = f'{book.name} - {shelve.id} - {book.author.name} - {book.isbn}'
                    result.append(res)
        return result

    @staticmethod
    def make_new_category(name, idx):
        return Category(name, idx)

    def salam(self):
        pass


class Writer(Human):
    def __init__(self, name, code):
        self.code = code
        super().__init__(name)

    def salam(self):
        pass


class Category:
    category_database = []

    def __init__(self, category_name, identifier):
        for category in self.__class__.category_database:
            if category_name == category.category_name:
                raise ValueError('category non duplicated.')

        self.category_name = category_name
        self.identifier = identifier
        self.__class__.category_database.append(self)

    def __len__(self):
        count = 0
        for idx, shelve in Shelve.shelve_database.items():
            if int(idx[2:]) == int(self.identifier):
                for _ in shelve.books:
                    count += 1
        return count

    def __repr__(self):
        return self.category_name


class Book:

    def __init__(self, name, pages, author: 'Writer', isbn, category: 'Category', price):
        if not isinstance(author, Writer):
            raise TypeError("writer must be instance of class Writer")
        if not isinstance(category, Category):
            raise TypeError('category must be instance of class Category')
        else:
            self.name = name
            self.__pages = pages
            self.__author = author
            self._isbn = isbn
            self._category = category
            self._price = price

    @property
    def pages(self):
        return self.__pages

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self._isbn

    @property
    def category(self):
        return self._category

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f'{self.category}: {self.name}'


class Shelve:
    shelve_identifier = 0
    shelve_database = {}

    def __init__(self, books: List[Book]):
        if not isinstance(books, list):
            raise TypeError("writer must be instance of class writer")
        for book in books:
            if not isinstance(book, Book):
                raise TypeError("writer must be instance of class writer")

        page = reduce(lambda x, y: x + y, map(lambda x: x.pages, books))
        if page > 10000:
            raise ValueError('pages of books must be less than 10000')
        else:
            self.books = books
            self.__class__.shelve_identifier += 1
            self.id = f'{self.__class__.shelve_identifier}-{books[0].category.identifier}'

        self.__class__.shelve_database[self.id] = self

    def __repr__(self):
        return f'{self.books}'


math = Category('math', 1234)
hendese = Category('hendese', 4321)
akbar = Writer('akbar', 111)
jafar = Writer('jafar', 555)
k1 = Book('riazi', 100, akbar, 12345, math, 1000)
k2 = Book('riazi2', 80, akbar, 54321, math, 2000)
k3 = Book('hendese3', 80, jafar, 12457, hendese, 1200)
k4 = Book('hendese tahlili', 280, jafar, 22331, hendese, 4500)
s1 = Shelve([k1, k2])
s2 = Shelve([k3, k4])
ketabdar = Librarian('mamad')

# k4.pages = 100
# k4.price = 100
# k4.category = math
# k4.author = akbar

print(k4.pages)
print(s1.books)
print(s2.books)

print(Shelve.shelve_database)

print(ketabdar.search_book_by_id(2131656))
print(ketabdar.search_book_by_name_or_id(111))

history = ketabdar.make_new_category('history', 1010)
print(history.category_name)
print(history.identifier)

print(len(math))
