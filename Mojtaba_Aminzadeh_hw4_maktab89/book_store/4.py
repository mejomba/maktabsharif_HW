class Book:
    def __init__(self, title, price, count):
        if count <= 0:
            raise ValueError("count of book must be positive")
        else:
            self.count = count
            self.title = title
            self.price = price

    def __repr__(self):
        return f'title: {self.title}, price: {self.price}, count: {self.count}'
