"""
    "Lists page" test cases
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.models import Item

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

class ItemModelTest(TestCase):
    """
        Tests related to the Item model
    """
    def test_saving_and_retrieving_items(self):
        """
            Create new records in the database and later tries to retrieve it
        """
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
