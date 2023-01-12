import sys


class Range:
    def __init__(self, start: int, end: int = None, step: int = 1) -> None:
        try:
            if not isinstance(start, int):
                raise TypeError('start must be "int"')
            if not isinstance(step, int):
                raise TypeError('step must be "int"')
            if end is not None and not isinstance(end, int):
                raise TypeError('end must be "int"')

            self.start = start
            if end is None:
                self.start = 0
                self.end = start
            else:
                self.end = end
            self.step = step

        except TypeError as err:
            print(err)
            sys.exit()

    def __iter__(self):
        if self.start < self.end and self.step > 0:
            while self.start < self.end:
                yield self.start
                self.start += self.step

        if self.start > self.end and self.step < 0:
            while self.start > self.end:
                yield self.start
                self.start += self.step

    def __next__(self):
        if self.start < self.end and self.step > 0:
            self.start += self.step
            return self.start - self.step

        if self.start > self.end and self.step < 0:
            self.start += self.step
            return self.start - self.step
        raise StopIteration

x = Range(5, 10, 1)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# print(next(x))
# print(next(x))
# for item in Range(5, 10, 1):
#     print(item)
# print('================')
# for i in range(-5, 5, 1):
#     print(i)