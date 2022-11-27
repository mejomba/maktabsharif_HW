class Person:
    def __init__(self, name, email, gender) -> None:
        self.name = name
        self.email = email
        self.gender = gender


class Writer(Person):
    def __init__(self, name, email, gender, code, genre) -> None:
        self.code = code
        self.genre = genre
        super().__init__(name, email, gender)


class Poet(Person):
    def __init__(self, email, style) -> None:
        self.style = style
        self.email = email
        super().__init__(name, email, gender)


class Researcher(Person):
    def __init__(self, name, email, gender, field, university) -> None:
        self.field = field
        self.university = university
        super().__init__(name, email, gender)
