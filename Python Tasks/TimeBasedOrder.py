# Import datetime and time classes
from datetime import datetime, time

print("Welcome to Restaurant Ordering System")

# Get current time
now = datetime.now()
current_time = now.time()

# Restaurant closing time (9:30 PM)
closing_time = time(21, 00)
formatted_closing_time = closing_time.strftime("%I:%M %p") # Format closing time to show only hour:minute AM/PM

# Check if restaurant is closed
if current_time > closing_time:
    print(f"Sorry, we can't accept orders at this time. We close at {formatted_closing_time} .")

else:
    # Menu dictionary
    menu = {
        1: ("Biryani", 250),
        2: ("Chicken Curry", 200),
        3: ("Naan", 50),
        4: ("Paneer Tikka", 180),
        5: ("Lassi", 60)
    }

    print("\nMenu:")
    for num, (name, price) in menu.items():
        print(f"{num}. {name} - ₹{price}")

    total = 0
    order_list = []   # List to store ordered items

    while True:
        choice = int(input("\nEnter item number (0 to finish): "))
        
        if choice == 0:
            break

        if choice in menu:
            name, price = menu[choice]
            qty = int(input("Quantity: "))
            item_total = price * qty

            total += item_total
            order_list.append((name, price, qty, item_total))  # Store full details

            print(f"Added {qty} x {name} = ₹{item_total}")
        else:
            print("Invalid choice!")

    # Show Order Summary
    print("\n===== Order Summary =====")
    for name, price, qty, item_total in order_list:
        print(f"{name} x{qty} @ ₹{price} = ₹{item_total}")

    # Show Final Total
    print("--------------------------")
    print(f"Total Bill: ₹{total}")
    print("Thank you for your order!")
