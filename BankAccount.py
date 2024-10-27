class BankAccount:
    def __init__(self, account_holder, account_number, bank_name, balance=0.0):
        """
        Initialize a Bank Account with essential details.

        Parameters:
        - account_holder (str): The name of the account holder.
        - account_number (str): The unique account number.
        - bank_name (str): The bank where the account is held.
        - balance (float): The initial balance in the account (default is 0.0).
        """
        self.account_holder = account_holder
        self.account_number = account_number
        self.bank_name = bank_name
        self.balance = balance

    def display_info(self):
        """
        Display the details of the bank account.
        """
        print("=== Bank Account Information ===")
        print(f"Account Holder   : {self.account_holder}")
        print(f"Account Number   : {self.account_number}")
        print(f"Bank Name        : {self.bank_name}")
        print(f"Balance          : ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Deposit an amount into the bank account.

        Parameters:
        - amount (float): The amount to deposit.
        
        Returns:
        - str: A message indicating the transaction status.
        """
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        self.balance += amount
        return f"${amount:.2f} has been deposited. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        """
        Withdraw an amount from the bank account.

        Parameters:
        - amount (float): The amount to withdraw.
        
        Returns:
        - str: A message indicating the transaction status.
        """
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"${amount:.2f} has been withdrawn. New balance: ${self.balance:.2f}"

    def get_balance(self):
        """
        Get the current balance of the bank account.

        Returns:
        - float: The current balance.
        """
        return self.balance