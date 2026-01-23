# Get the number of products the customer wants to order
n = int(input("Enter number of products: "))

# Store product details
prod_details = {
    "prod1": {"item": "apple", "cost": 20},
    "prod2": {"item": "banana", "cost": 10},
    "prod3": {"item": "chocolate", "cost": 5},
    "prod4": {"item": "drink", "cost": 80}
}

# Keep track of how much user is spending
total_amount = 0

# Ask for the initial n products
for i in range(n):
    # Get product name from customer
    product = input("Enter product name: ")
    quantity = int(input("Number of quantity: "))

    found = False

    # Search through all products
    for prod_id in prod_details:
        prod = prod_details[prod_id]

        if prod["item"] == product:
            print("Product Name:", prod["item"])
            itemCost = quantity * prod["cost"]
            print("Amount:", itemCost)

            total_amount += itemCost
            found = True
            break
    
    if not found:
        print("No Product Found")

    # Display current total amount
    print(f"\n--- Total Amount: {total_amount} ---")

# Ask if user wants to add more products (one at a time)
while True:
    choice = input("\nDo you want to spend more? (y/n): ")

    if choice.lower() == 'y':
        # Add one more product
        product = input("Enter product name: ")
        quantity = int(input("Number of quantity: "))

        found = False

        # Search through all products
        for prod_id in prod_details:
            prod = prod_details[prod_id]

            if prod["item"] == product:
                print("Product Name:", prod["item"])
                itemCost = quantity * prod["cost"]
                print("Amount:", itemCost)

                total_amount += itemCost
                found = True
                break
        
        if not found:
            print("No Product Found")

        # Display current total amount
        print(f"\n--- Total Amount: {total_amount} ---")
        continue   # Ask again if they want to spend more

    elif choice.lower() == 'n':
        print("\nThank You For Your Order!")
        print("Final Bill Amount:", total_amount)
        break

    else:
        print("Invalid Choice, Exiting...")
        break
