"""
    "Lists page" test cases
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    """
        asdf
    """
    def test_root_url_resolves_to_home_page_view(self):
        """
            Insert docstring
        """
        found = resolve('/')
        self.assertEqual(found.func, home_page)
