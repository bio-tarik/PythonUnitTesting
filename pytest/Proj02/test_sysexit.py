"""
Learning unit testing on Python using py.test.
Tutorial: docs.pytest.org/en/latest/getting-started.html#our-first-test-run
"""
import pytest


def func():
    """
        Automatically raises error
    """
    raise SystemExit(1)


def test_mytest():
    """
        Tests wheter or not the function returns an error
    """
    with pytest.raises(SystemExit):
        func()
