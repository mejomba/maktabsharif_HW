class Book:
    def __init__(self, title, price, count):
        try:
            assert count > 0, "count of book can't be 0"
            self.count = count
        except AssertionError as e:
            print(e)
        self.title = title
        self.price = price

    def __repr__(self):
        return f'title: {self.title}, price: {self.price}, count: {self.count}'