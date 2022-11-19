from typing import Generator

def range(start:int, end:int=None, step:int=1) -> Generator:
    """
    :param start: int
    :param end: optional
    :param step: 1
    :return: generator for sequence of integer number
    """
    try:
        if not isinstance(start, int):
            raise TypeError(f'range expected type "int" but given type {type(start)}')
        while start != end:
            yield start
            start += step

    except TypeError as e:
        print(e)

    pass

for i in range(1, 10):
    print(i)
