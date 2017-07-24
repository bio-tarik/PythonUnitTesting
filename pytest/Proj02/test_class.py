"""
Learning unit testing on Python using py.test.
Tutorial: docs.pytest.org/en/latest/getting-started.html#our-first-test-run
"""


class TestClass(object):
    """
        Generic test class
    """

    def test_one(self):
        """
            Tests if the string 'this' contains 'h'
        """
        string = "this"
        assert 'h' in string

    def test_two(self):
        """
            Check if string object has the 'check' attribute
        """
        string = "hello"
        assert hasattr(string, 'check')
