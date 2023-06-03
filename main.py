class Customer():
    def __init__(self, username):
        self.username = username
        
class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order():
    def __init__(self, customer):
        self.customer = customer
        self.order_items = []
        
        
    def add_items(self, item):
        self.order_items.append(item)
        
    def remove_items(self, item):
        self.order_items.remove(item)
    
    
class OrderItem():
    def __init__(self, product, quantity):
        pass