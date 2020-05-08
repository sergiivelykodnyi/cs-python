from unittest import TestCase


def string_reverse(string):
    result = ""

    for character in string:
        result = character + result

    return result


class TestStringReverse(TestCase):
    """Test string_reverse() function"""

    def test_return_value(self):
        """test that string_reverse() returns reversal string"""
        self.assertEqual(string_reverse("Hello World!"), "!dlroW olleH")


def list_reverse(list_):
    result = []

    for item in list_:
        result = [item] + result

    return result


class TestListReverse(TestCase):
    """Test list_reverse() function"""

    def test_return_value(self):
        """test that list_reverse() returns reversal list"""
        self.assertListEqual(list_reverse([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])
