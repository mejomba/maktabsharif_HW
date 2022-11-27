from people import Person, Poet, Writer, Researcher
from typing import List, Union


class Asar:
    def __init__(self, title: str, authors: Union[List[Person], Person]) -> None:
        self.title = title
        self.authors = authors


class Book(Asar):
    def __init__(self, title: str, authors: List[Writer], isbn: int, publisher: str) -> None:
        assert isinstance(authors, list), 'book authors must be [writer, writer, ...]'
        for author in authors:
            assert isinstance(author, Writer), 'book authors must be [writer, writer, ...]'
        self.isbn = isbn
        self.publisher = publisher
        super().__init__(title, authors)

    def get_number_of_authors(self):
        count = 0
        for _ in self.authors:
            count += 1
        return count


class Poetry(Asar):
    def __init__(self, title, authors: Poet, literary_format):
        try:
            assert isinstance(authors, Poet), 'Error: the poetry can only have one author of type Poet'
        except AssertionError as e:
            print(e)
        self.literary_format = literary_format
        super().__init__(title, authors)


class Paper(Asar):
    def __init__(self, title, authors: List[Researcher], journal_name, publish_date):
        assert isinstance(authors, list), 'paper authors must be [Researcher, Researcher, ...]'
        for author in authors:
            assert isinstance(author, Researcher), 'paper authors must be [Researcher, Researcher, ...]'
        self.journal_name = journal_name
        self.publish_date = publish_date
        super().__init__(title, authors)

    def get_number_of_authors(self):
        return len(self.authors)

