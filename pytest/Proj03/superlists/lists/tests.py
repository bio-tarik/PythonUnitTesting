"""
    Lists page test cases
"""
from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    """
        Class created to test if I'm able to use django's test structure
    """
    def test_bad_maths(self):
        """
            Silly and useless test with no meaning other than failing :)
        """
        self.assertEqual(1 + 1, 3)
