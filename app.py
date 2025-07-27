class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        name (str): The name of the account holder.
        balance (float): The current balance of the account. Default is 0.

    Methods:
        deposit(amount):
            Adds a specified amount to the balance if the amount is positive.
        withdraw(amount):
            Deducts a specified amount from the balance if sufficient funds are available.
        check_balance():
            Prints the current balance of the account.
    """

    def __init__(self, name, balance=0):
        """
        Constructs all the necessary attributes for the bank account object.

        Args:
            name (str): The name of the account holder.
            balance (float, optional): The initial balance. Default is 0.
        """
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the bank account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """
        Withdraw money from the bank account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        """
        Display the current account balance.

        Returns:
            None
        """
        print(f"Current balance for {self.name}: ${self.balance}")


def main():
    """
    The main function to run the bank account CLI application.

    Provides options to deposit, withdraw, check balance, or exit.
    """
    print("Welcome to the Python Bank!")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
