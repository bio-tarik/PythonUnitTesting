"""
    "Lists page" test cases
"""
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.shortcuts import render
from django.test import TestCase

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

    def test_home_page_can_save_a_POST_request(self):
        """
            Post content to home_page and sees if it can handle it properly
        """
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
