"""
    Learning unit testing on Python using py.test.
    Tutorial: https://docs.pytest.org/en/latest/assert.html
"""


class Foo(object):
    """
        Type created to exemplify the usage of conftest.py
    """
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def test_compare():
    """
        Compares two instances of the Foo class
    """
    a_foo = Foo(1)
    another_foo = Foo(2)
    assert a_foo == another_foo
