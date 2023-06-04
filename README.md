# shopping-cart
A basic shopping cart that can add order items, remove and a return a shipping status based on the digital flag of a product. This project is a personal guide to understanding the concepts of TDD


# 5 models 
#   - Customer
#        - Has a name
#   - Product
#        - Has name, price, is_digital flag,
#   - Order
#       - Has a customer
#       - A method to add order items
#       - A method to remove order items
#       - A method that returns shipping if a product is digital or not
#       - A method that returns the total amount of product in an order
#       - A method that returns the total quantity of items in a cart order
#   - OrderItem
#       - Has a product, quantity
#   - Order
#        - Has a customer, order_date, is_complete status, transaction_id
#       - A method that returns shipping if a product is digital or not
#       - A method that returns the total amount of produc
#   - Order
#        - Has a customer, order_date, is_complete status, transaction_id
#       - A method that returns shipping if a product is digital or not
#       - A method that returns the total amount of product in an order
#       - A method that returns the total quantity of itemt in an order
#       - A method that returns the total quantity of item
#     
#   - Order
#        - Has a customer, order_date, is_complete status, transaction_id
#       - A method that returns shipping if a product is digital or not
#       - A method that returns the total amount of product in an order
#       - A method that returns the total quantity of item  - A method that checks the total of products of the orderitem
#   - ShippingAddress
#        - Has customer, order, address, date, ...
