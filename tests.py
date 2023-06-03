import unittest
from main import Order, Customer, Product, OrderItem


class TestOrder(unittest.TestCase):
    def test_add_order_items(self):
        customer = Customer("Tim")
        order = Order(customer)
        
        product_1 = Product("Oranges", 20)
        product_2 = Product("Mangoes", 30)
        product_3 = Product("Salad", 40)
        
        order_item_1 = OrderItem(product_1, 3)
        order_item_2 = OrderItem(product_2, 6)
        
        order.add_items(order_item_1)
        order.add_items(order_item_2)
        
        self.assertEqual(len(order.order_items), 2)
        self.assertIn(order_item_1, order.order_items)
        self.assertEqual(order.order_items[0], order_item_1)
        
        
    def test_remove_order_items(self):
        customer = Customer("Tim")
        order = Order(customer)
        
        product_1 = Product("Oranges", 20)
        product_2 = Product("Mangoes", 30)
        product_3 = Product("Salad", 40)
        
        order_item_1 = OrderItem(product_1, 3)
        order_item_2 = OrderItem(product_2, 6)
        
        order.add_items(order_item_1)
        order.add_items(order_item_2)
        
        order.remove_items(order_item_1)
        
        self.assertEqual(len(order.order_items), 1)
        self.assertNotIn(order_item_1, order.order_items)
        self.assertIn(order_item_2, order.order_items)
        
        
        
if __name__ == "__main__":
    unittest.main()