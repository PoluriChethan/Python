# ATM class definition
class ATM:
    
    # Constructor method (called when object is created)
    def __init__(self, name, password, pin, balance = 0):
        self.name = name                  # Public attribute (account holder name)
        self.__password = password        # Private attribute (password)
        self.__pin = pin                  # Private attribute (PIN)
        self.__balance = balance          # Private attribute (account balance)
        self.__transaction = []           # Private list to store transaction history

    # Method to login into ATM
    def login(self):
        enter_name = input("Enter Name : ")
        enter_password = input("Enter Password : ")
        enter_pin = int(input("Enter Pin : "))

        # Check if entered name matches
        if enter_name != self.name:
            print("Name is Not Matching")
            return False
        
        # Check if password and pin match
        elif enter_password == self.__password and enter_pin == self.__pin:
            print("Login Successfull")
            return True
        
        # If password or pin is incorrect
        else:
            print("Incorrect Password Or Pin")
            return False
        

    # Method to deposit money
    def deposit(self, amount):
        self.__balance += amount                 # Add amount to balance
        self.__transaction.append(amount)        # Store transaction
        print("Amount Successfully Deposited")
        print("Amount Deposited : ", amount)
        print("Total Amount Available in Account After Money Deposited : ", self.__balance)


    # Method to withdraw money
    def withdraw(self, amount):
        # Check if sufficient balance is available
        if amount <= self.__balance:
            self.__balance -= amount             # Deduct amount
            self.__transaction.append(amount)   # Store withdrawal as negative
            print("Please Collect your Cash")
            print("Amount Withdrawn : ", amount)
            print("Total Amount Available in Account After Money Withdraw : ", self.__balance)
        else:
            print("Insufficient Balance")


    # Method to check current balance
    def check_balance(self):
        print("Available Balance :", self.__balance)


    # Method to show transaction history
    def transaction_history(self):
        print(" ---------- Transaction History ---------- ")
        for count, i in enumerate(self.__transaction, start = 1):
            print(f"Transaction {count} : {i}")


# Creating ATM object
atm = ATM("Chethan", "2149", 1980, 15000)

# First login check
if atm.login():
    
    # Infinite loop until user exits
    while True:
        print("1. Deposit ")
        print("2. Withdraw ")
        print("3. Check Balance ")
        print("4. Transaction History ")
        print("5. Exit ")

        choice = int(input("Enter the Choice : "))

        if choice == 1:
            amount = int(input("Enter the Deposit Amount : "))
            atm.deposit(amount)

        elif choice == 2:
            amount = int(input("Enter the Withdraw Amount : "))
            atm.withdraw(amount)

        elif choice == 3:
            atm.check_balance()

        elif choice == 4:
            atm.transaction_history()

        elif choice == 5:
            print("Thank you for Using ATM")
            break

        else:
            print("Invalid Choice")
