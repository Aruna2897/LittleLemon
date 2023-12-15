from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=8.00, Inventory=10)
        self.assertEqual(item, "IceCream : 8.00")