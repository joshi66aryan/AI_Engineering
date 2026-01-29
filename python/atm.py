class ATM:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__pin = pin         
        self.balance = balance

    def authenticate(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.__pin:
            print("Login successful!\n")
            return True
        else:
            print("Incorrect PIN. Access denied.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")


if __name__ == "__main__":
    atm = ATM(name="Aryan", pin="1234", balance=1000)

    if atm.authenticate():
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                atm.check_balance()
            elif choice == "2":
                atm.deposit()
            elif choice == "3":
                atm.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid choice. Try again.")

