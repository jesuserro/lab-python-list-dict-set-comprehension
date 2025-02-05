# 1. Define a function named `initialize_inventory` that takes `products` as a parameter. 
# Inside the function, implement the code for initializing the inventory dictionary using a loop and user input.
def initialize_inventory(products):
    inventory = {}
    for product in products:
        # inventory[product] = int(input(f"How many {product}s do we have? "))
        inventory = {product: int(input(f"Enter the quantity of {product}s available: ")) for product in products}
    return inventory

# 2. Define a function named `get_customer_orders` that takes no parameters. 
# Inside the function, implement the code for prompting the user to enter the product names using a loop. 
# The function should return the `customer_orders` set.
def get_customer_orders():
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

# 3. Define a function named `update_inventory` that takes `customer_orders` and `inventory` as parameters. 
# Inside the function, implement the code for updating the inventory dictionary based on the customer orders.
def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        inventory[product] -= 1
    return

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
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")