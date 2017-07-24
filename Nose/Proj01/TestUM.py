"""
Learning unit testing on Python using nose.
Tutorial: http://pythontesting.net/framework/nose/nose-introduction/
"""
from unnecessary_math import multiply
from nose import with_setup


def my_setup_function():
    """
        Test setup function
    """
    pass


def my_teardown_function():
    """
        Test teardown function
    """
    pass


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    """
        Check if 3x4=12
    """
    assert multiply(3, 4) == 12


@with_setup(my_setup_function, my_teardown_function)
def test_strings_a_3():
    """
        Check if a string parameter gets printed 3 times
    """
    assert multiply('a', 3) == 'aaa'


class TestUM(object):
    """
        My very first test class using Nose to run tests
    """

    def setup(self):
        """
            Test setup function
        """
        pass

    def teardown(self):
        """
            Test teardown function
        """
        pass

    @classmethod
    def setup_class(cls):
        """
            Class setup method
        """
        pass

    @classmethod
    def teardown_class(cls):
        """
            Class teardown method
        """
        pass

    @staticmethod
    def test_numbers_5_6():
        """
            Check if 5x6=30
        """
        assert multiply(5, 6) == 30

    @staticmethod
    def test_strings_b_2():
        """
            Check if a string parameter gets printed 2 times
        """
        assert multiply('b', 2) == 'bb'
