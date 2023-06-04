class Customer():
    def __init__(self, username):
        self.username = username
        
class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_digital = False
        
    def __str__(self):
        return self.name

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
    
    def get_quantity(self):
        total = sum([item.quantity for item in self.order_items])
        return total
    
    def can_be_shipped(self):
        shipping = False
        for item in self.order_items:
            if item.product.is_digital == False:
                shipping = True
                
        return shipping
    
    def display_cart(self):
        print("Customer", self.customer.username)
        print()
        for item in self.order_items:
            print("Product", item.product)
            print("Price", item.product.price)
            print("Quantity", item.quantity)
            print("Can be shipped", self.can_be_shipped())
            print()
                
    
class OrderItem():
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def get_total(self):
        return self.product.price * self.quantity
    
    
    
customer = Customer("Tim")
order = Order(customer)
        
product_1 = Product("Oranges", 20)
product_2 = Product("Mangoes", 30)
product_3 = Product("Salad", 40)
        
order_item_1 = OrderItem(product_1, 3)
order_item_2 = OrderItem(product_2, 6)
        
order.add_items(order_item_1)
order.add_items(order_item_2)

order.display_cart()