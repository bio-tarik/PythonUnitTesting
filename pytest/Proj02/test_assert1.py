"""
    Learning unit testing on Python using py.test.
    Tutorial: https://docs.pytest.org/en/latest/assert.html
"""
import pytest


def func():
    """
        Automatically returns 3
    """
    return 3


def error_123_func():
    """
        Simply throws an error message
    """
    raise ValueError("Exception 123 raised")


def test_func():
    """
        Tests if 3 = 4
    """
    assert func() == 4


def test_odd():
    """
        Checks if 3 is an even number
    """
    number = 3
    assert number % 2 == 0, "value was odd, should be even"


def test_zero_division():
    """
        Deliberately tries to divide by zero and thus\
        tries to destroy the world
    """
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_recursion_depth():
    """
        Tests that causes an infinite function call
    """
    with pytest.raises(RuntimeError) as excinfo:
        def infinite_func():
            """
                Infinite recursion function
            """
            infinite_func()
        infinite_func()
    assert 'maximum recursion' in str(excinfo.value)


def test_match():
    """
        Tests whether an error message contains '123'
    """
    with pytest.raises(ValueError) as excinfo:
        error_123_func()
    excinfo.match(r'.* 123 .*')
