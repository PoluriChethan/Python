# Get customer name from user input
name = input("Enter the name: ")
# Get customer PIN from user input and convert to integer
pin = int(input("Enter the pin: "))

# Dictionary containing customer account details with name, PIN, and balance amount
details = {
    "cust1": {"name": "chethan", "pin": 2149, "amount": 5000},
    "cust2": {"name": "leela", "pin": 1980, "amount": 3000},
    "cust3": {"name": "sai", "pin": 1234, "amount": 1000}
}

# Flag to check if customer exists in the system
isExist = False
# Variable to store the matched customer object
found_customer = None

# Loop through all customers to verify name and PIN match
for cust_id in details:
    customer = details[cust_id]
    # Check if name and PIN match the entered credentials
    if(customer["name"] == name and customer["pin"] == pin):
        isExist = True
        found_customer = customer
        break

# If customer is authenticated, proceed with withdrawal process
if isExist:
    while True:
        # Get the withdrawal amount from the customer
        withdraw_amount = int(input("Enter the Amount To  Withdraw:"))
        # Check if withdrawal amount exceeds available balance
        if withdraw_amount > found_customer["amount"]:
            print("Insufficient Balance")
        else:
            # Deduct the withdrawal amount from customer's balance
            found_customer["amount"] -= withdraw_amount
            print("Amount Debited Successfully")
            print("Available Amount After Money Debited: ", found_customer["amount"])

            # Ask if customer wants to perform another transaction
            choice = input("Do you want to withdraw more money? (y/n): ")
            if choice.lower() == 'n':
                print("Thank You For using ATM")
                break
            elif choice.lower() == 'y':
                continue
            else:
                print("Invalid Choice")
else:
    # Display error if customer credentials are invalid
    print("Invalid Details")
