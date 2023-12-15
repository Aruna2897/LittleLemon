from django.test import TestCase
from restaurant.models import Menu
import json
from django.urls import reverse

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Pizza", price=10.00, inventory=20)
        Menu.objects.create(title="Burger", price=15.00, inventory=15)
        Menu.objects.create(title="Cake", price=5.00, inventory=25)

    def test_getall(self):
        menus = Menu.objects.all() 
        serialized_data = json.dumps([{'title': menu.title, 'price':menu.price, 'inventory': menu.price} for menu in menus])

        response = self.client.get(reverse('menu-items'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), serialized_data)

