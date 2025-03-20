import datetime
import random
class ATM:
    def __init__(self):
        self.balance = 1000000
        self.pin = "2003"
        self.transaction_history = []
        self.max_attempts = 3

    def verify_pin(self):
        """Verify user's PIN with maximum attempts"""
        attempts = 0
        while attempts < self.max_attempts:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                attempts += 1
                remaining = self.max_attempts - attempts
                print(f"Incorrect PIN. {remaining} attempts remaining.")
        print("Too many incorrect attempts. Card blocked!")
        return False

    def check_balance(self):
        """Display current balance"""
        print(f"\nCurrent Balance: ${self.balance:.2f}")
        self.transaction_history.append(f"Balance checked: ${self.balance:.2f} on {datetime.datetime.now()}")

    def deposit(self):
        """Handle cash deposit"""
        try:
            amount = float(input("\nEnter amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                print(f"Successfully deposited ${amount:.2f}")
                print(f"New balance: ${self.balance:.2f}")
                self.transaction_history.append(f"Deposited ${amount:.2f} on {datetime.datetime.now()}")
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("Invalid amount entered.")

    def withdraw(self):
        """Handle cash withdrawal"""
        try:
            amount = float(input("\nEnter amount to withdraw: $"))
            if amount <= 0:
                print("Please enter a positive amount.")
            elif amount > self.balance:
                print("Insufficient funds!")
            else:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}")
                print(f"New balance: ${self.balance:.2f}")
                self.transaction_history.append(f"Withdrew ${amount:.2f} on {datetime.datetime.now()}")
        except ValueError:
            print("Invalid amount entered.")

    def change_pin(self):
        """Change ATM PIN"""
        old_pin = input("\nEnter current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN successfully changed!")
                self.transaction_history.append(f"PIN changed on {datetime.datetime.now()}")
            else:
                print("New PIN must be 4 digits!")
        else:
            print("Incorrect current PIN!")

    def show_history(self):
        """Display transaction history"""
        print("\nTransaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

def main():
    atm = ATM()
    print("Welcome to pata pata Bank ATM")

    if not atm.verify_pin():
        return
    while True:
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.deposit()
        elif choice == "3":
            atm.withdraw()
        elif choice == "4":
            atm.change_pin()
        elif choice == "5":
            atm.show_history()
        elif choice == "6":
            print("\nThank you for using my Bank ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()