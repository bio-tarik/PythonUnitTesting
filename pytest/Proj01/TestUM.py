"""
Learning unit testing on Python using py.test.
Tutorial: http://pythontesting.net/framework/pytest/pytest-introduction/
"""
from unnecessary_math import multiply


def setup_module(module):
    """
        Module setup method
    """
    print("setup_module      module:%s" % module.__name__)


def teardown_module(module):
    """
        Module teardown method
    """
    print("teardown_module   module:%s" % module.__name__)


def setup_function(function):
    """
        Test function setup
    """
    print("setup_function    function:%s" % function.__name__)


def teardown_function(function):
    """
        Test function teardown
    """
    print("teardown_function function:%s" % function.__name__)


def test_numbers_3_4():
    """
        Check if 3x4=12
    """
    assert multiply(3, 4) == 12


def test_strings_a_3():
    """
        Check if a string parameter gets printed 3 times
    """
    assert multiply('a', 3) == 'aaa'


class TestUM:
    """
        Test class to be used with py.test
    """

    def setup(self):
        """
            Function setup
        """
        print("setup             class:TestStuff")

    def teardown(self):
        """
            Function teardown
        """
        print("teardown          class:TestStuff")

    @classmethod
    def setup_class(cls):
        """
            Class setup method
        """
        print("setup_class       class:%s" % cls.__name__)

    @classmethod
    def teardown_class(cls):
        """
            Class teardown method
        """
        print("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        """
            Method setup
        """
        print("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        """
            Method teardown
        """
        print("teardown_method   method:%s" % method.__name__)

    def test_numbers_5_6(self):
        """
            Check if 5x6=30
        """
        assert multiply(5, 6) == 30

    def test_strings_b_2(self):
        """
            Check if a string parameter gets printed 2 times
        """
        assert multiply('b', 2) == 'bb'
