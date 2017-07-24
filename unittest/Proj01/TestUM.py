
"""
Learning unit testing on Python using unittest.
Tutorial: http://pythontesting.net/framework/unittest/unittest-introduction/
"""

import unittest
from unnecessary_math import multiply


class TestUM(unittest.TestCase):
    """
        My very first test class
    """

    def setup(self):
        """
            Test class setup method
        """
        pass

    def test_numbers_3_4(self):
        """
            Check if 3x4=12
        """
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        """
            Check if a string parameter gets printed 3 times
        """
        self.assertEqual(multiply('a', 3), 'aaa')


if __name__ == '__main__':
    unittest.main()
