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
        
    def get_total_amount(self):
        total  = sum([item.get_total() for item in self.order_items])
        return total
    
    
class OrderItem():
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def get_total(self):
        return self.product.price * self.quantity