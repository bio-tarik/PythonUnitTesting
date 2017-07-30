"""
    "Lists page" test cases
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    """
        "Lists page" test cases
    """
    def test_root_url_resolves_to_home_page_view(self):
        """
            Checks if root page redirects correctly to the home page view
        """
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """
            Parses the obtained html and check wether its contents matches
            that from the homepage
        """
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
