"""
Learning unit testing on Python using py.test.
Tutorial: docs.pytest.org/en/latest/getting-started.html#our-first-test-run
"""


def func(number):
    """
        Adds 1 to the "number" parameter
    """
    return number + 1


def test_answer():
    """
        Tests if 3 + 1 = 5
    """
    assert func(3) == 5
