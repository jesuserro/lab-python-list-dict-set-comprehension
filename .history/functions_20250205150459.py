# 1. Define a function named `initialize_inventory` that takes `products` as a parameter. 
# Inside the function, implement the code for initializing the inventory dictionary using a loop and user input.
def initialize_inventory(products):
    inventory = {}
    # for product in products:
    #    inventory[product] = int(input(f"How many {product}s do we have? "))
    inventory = {product: int(input(f"Enter the quantity of {product}s available: ")) for product in products}
    return inventory

# 2. Define a function named `get_customer_orders` that takes no parameters. 
# Inside the function, implement the code for prompting the user to enter the product names using a loop. 
# The function should return the `customer_orders` set.
def get_customer_orders_0():
    customer_orders = set()
    customer_orders_num = 0
    while True:
        add_another = input(f"Do you want to add product number {customer_orders_num + 1}? (yes/no) ")
        if add_another.lower() == "yes":
            customer_orders_num += 1
            product = input("Enter the name of the product you want to order: ")
            customer_orders.add(product)
        else:
            break
    return customer_orders

# 2. Modify the function get_customer_orders so it prompts the user to enter the number of customer orders and gathers the product names using a loop and user input. 
# Use comprehension.
def get_customer_orders():
    customer_orders = set()
    customer_orders_num = int(input("Enter the number of products you want to order: "))
    customer_orders = {input(f"Enter the name of product number {i + 1}: ") for i in range(customer_orders_num)}
    return customer_orders

# 3. Define a function named `update_inventory` that takes `customer_orders` and `inventory` as parameters. 
# Inside the function, implement the code for updating the inventory dictionary based on the customer orders.
def update_inventory_0(customer_orders, inventory):
    for product in customer_orders:
        inventory[product] -= 1
    return

# 4. Modify the update_inventory function to remove the product from the inventory if its quantity becomes zero after fulfilling the customer orders. 
# Use comprehension to filter out the products with a quantity of zero from the inventory.
def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        inventory[product] -= 1
    inventory = {product: quantity for product, quantity in inventory.items() if quantity > 0}
    return inventory

# 4. Define a function named `calculate_order_statistics` that takes `customer_orders` and `products` as parameters. 
# Inside the function, implement the code for calculating the order statistics (total products ordered, and percentage of unique products ordered). 
# The function should return these values.
def calculate_order_statistics(customer_orders, products):
    total_products_ordered = len(customer_orders)
    percentage_products_ordered = (total_products_ordered / len(products)) * 100
    return total_products_ordered, percentage_products_ordered

# 5. Define a function named `print_order_statistics` that takes `order_statistics` as a parameter. 
# Inside the function, implement the code for printing the order statistics.
def print_order_statistics(order_statistics):
    total_products_ordered, percentage_products_ordered = order_statistics
    print(f"Order Statistics:\nTotal Products Ordered: {total_products_ordered}\nPercentage of Products Ordered: {percentage_products_ordered}%")

# 6. Define a function named `print_updated_inventory` that takes `inventory` as a parameter. 
# Inside the function, implement the code for printing the updated inventory.
def print_updated_inventory(inventory):
    inventory_list = [f"- {product}: {quantity}" for product, quantity in inventory.items()]
    print("\n".join(inventory_list))




    print("\n".join([f"{product}: {quantity}" for product, quantity in inventory.items()]))

# 3. Add a new function to calculate the total price of the customer order. 
# For each product in customer_orders, prompt the user to enter the price of that product. 
# Use comprehension to calculate the total price. 
# Note: assume that the user can only have 1 unit of each product.
def calculate_total_price(customer_orders):
    total_price = sum([float(input(f"Enter the price of {product}: ")) for product in customer_orders])
    return total_price