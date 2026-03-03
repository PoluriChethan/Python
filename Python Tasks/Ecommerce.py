print("=== Ecommerce Shopping Cart ===")

# Dictionary storing product details
# Key = item number
# Value = (Product Name, Price)
products = {
    1: ("iPhone 15", 80000),
    2: ("MacBook Pro", 150000),
    3: ("Nike T-Shirt", 1500),
    4: ("Adidas Shoes", 8000),
    5: ("AirPods", 20000),
    6: ("Watch", 5000)
}

# Display all available products
print("\nProducts:")
for num, (name, price) in products.items():
    print(f"{num}. {name} - ₹{price:,}")  # :, formats number with commas

# List to store cart items
# Each item will be stored as (name, price, quantity)
cart = []

# Variable to store total bill amount
total = 0

# Loop runs until user finishes shopping
while True:
    
    # Show current total amount
    print(f"\nCurrent total: ₹{total:,}")
    
    # Take item number from user
    # 0 = finish shopping
    # -1 = remove last added item
    item_no = int(input("Enter item no (0=finish, -1=remove last): "))
    
    # If user enters 0, stop shopping
    if item_no == 0:
        break

    # If user wants to remove last item and cart is not empty
    elif item_no == -1 and cart:
        name, price, qty = cart.pop()  # Remove last added item
        total -= price * qty           # Deduct its cost from total
        print(f"Removed {name} x{qty}")

    # If entered item number exists in products list
    elif item_no in products:
        name, price = products[item_no]      # Get product details
        qty = int(input("Quantity: "))       # Ask for quantity
        cart.append((name, price, qty))      # Add item to cart
        total += price * qty                 # Add cost to total
        print(f"Added {name} x{qty} = ₹{price*qty:,}")

    # If invalid item number entered
    else:
        print("Wrong item number!")

# After exiting loop, display final cart
print("\n=== Your Cart ===")

# Print each item in cart
for name, price, qty in cart:
    print(f"- {name} x{qty} = ₹{price*qty:,}")

# Display final total amount
print(f"Final Total: ₹{total:,}")

# Thank you message
print("Thank you for shopping!")
