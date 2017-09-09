"""
    "Lists page" test cases
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.models import Item
from lists.models import List
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

class ListAndItemModelsTest(TestCase):
    """
        Tests related to the Item model
    """
    def test_saving_and_retrieving_items(self):
        """
            Create new records in the database and later tries to retrieve it
        """
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

class ListViewTest(TestCase):
    """
        Tests related to the to-do items viewing page
    """
    def test_displays_all_list_items(self):
        """
            Checks whether or not the created items are being displayed
        """
        list_ = List.objects.create()
        Item.objects.create(text = 'itemey 1', list=list_)
        Item.objects.create(text = 'itemey 2', list=list_)

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_list_template(self):
        """
            Insert docstring
        """
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

class NewListItem(TestCase):
    """
        Insert docstring
    """
    def test_can_save_a_POST_request(self):
        """
            Post content to home_page and sees if it can handle it properly
        """
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
