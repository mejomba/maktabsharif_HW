from people import Person, Poet, Writer, Researcher
from typing import List, Union
from mahsol import Mahsol


class Asar(Mahsol):
    def __init__(self, title: str, price: int, count: int, authors: Union[List[Person], Person]) -> None:
        # self.title = title
        self.authors = authors
        super().__init__(title, price, count)


class Book(Asar):
    def __init__(self, title: str, price, count, authors: List[Writer], isbn: int, publisher: str) -> None:
        if not isinstance(authors, list):
            raise TypeError('book authors must be [writer, writer, ...]')
        for author in authors:
            if not isinstance(author, Writer):
                raise TypeError('book authors must be [writer, writer, ...]')
        self.authors = authors
        self.isbn = isbn
        self.publisher = publisher
        super().__init__(title, price, count, authors)

    def get_number_of_authors(self):
        count = 0
        for _ in self.authors:
            count += 1
        return count


class Poetry(Asar):
    def __init__(self, title, price, count, authors: Poet, literary_format):
        if not isinstance(authors, Poet):
            raise TypeError('Error: the poetry can only have one author of type Poet')
        self.literary_format = literary_format
        super().__init__(title, price, count, authors)


class Paper(Asar):
    def __init__(self, title, price, count, authors: List[Researcher], journal_name, publish_date):
        if not isinstance(authors, list):
            raise TypeError('Error: paper authors must be [Researcher, Researcher, ...]')
        for author in authors:
            if not isinstance(author, Researcher):
                raise TypeError('Error: paper authors must be [Researcher, Researcher, ...]')
        self.journal_name = journal_name
        self.publish_date = publish_date
        super().__init__(title, price, count, authors)

    def get_number_of_authors(self):
        return len(self.authors)

