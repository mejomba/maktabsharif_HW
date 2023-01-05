import unittest


class CustomAssertions:
    def my_custom_assertion(self):
        # check some condition or ...
        raise AssertionError('this is my custom assertion')


class TestCase(unittest.TestCase, CustomAssertions):

    def test_my_assertion(self):
        self.my_custom_assertion()


if __name__ == '__main__':
    unittest.main()