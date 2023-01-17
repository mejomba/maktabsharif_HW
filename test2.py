import unittest


def func():
    5/0
    try:
        x = 5/0
    except ZeroDivisionError:
        return 'zero'


# print(func())

class TestExcepiont(unittest.TestCase):
    def test_func(self):
        self.assertRaises(ZeroDivisionError, func)


if __name__ == "__main__":
    unittest.main()