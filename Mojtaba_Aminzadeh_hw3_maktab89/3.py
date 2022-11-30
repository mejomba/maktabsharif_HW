from typing import Generator


def range(start: int, end: int = None, step: int = 1) -> Generator:

    """
    :param start: int
    :param end: int [optional] if not present, replace with `start` and `start` set to 0
    :param step: int [optional]
    :return: generator for sequence of integer number

    Example1: range(1, 5) -> 1, 2, 3, 4
    Example2: range(5) -> 0, 1, 2, 3, 4
    Example3: range(1, 7, 2) -> 1, 3, 5
    """

    if end is None:
        end = start
        start = 0

    if step == 0:
        raise ValueError(f'step value can not be zero')
    if not isinstance(start, int):
        raise TypeError(f'range expected type "int" but given type {type(start)}')
    elif not isinstance(end, int):
        raise TypeError(f'range "end" expected type "int" but given type {type(end)}')
    elif not isinstance(step, int):
        raise TypeError(f'range "step" expected type "int" but given type {type(step)}')

    if start < end and step > 0:
        while start < end:
            yield start
            start += step
    elif start > end and step < 0:
        while start > end:
            yield start
            start += step


for i in range(5, 10):
    print(i)
