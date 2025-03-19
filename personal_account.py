# File: src/personal_account.py

from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return (f"Amount: {self.amount}, Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}, "
                f"Type: {self.transaction_type}")

class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            transaction = Amount(amount, 'DEPOSIT')
            self.transactions.append(transaction)
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            transaction = Amount(amount, 'WITHDRAWAL')
            self.transactions.append(transaction)
            self.balance -= amount
            return True
        else:
            return False

    def print_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self

if __name__ == "__main__":
    account = PersonalAccount(12345, "John Doe")

    account.deposit(1000)
    account.withdraw(500)
    account + 200  # Using __add__
    account - 100  # Using __sub__

    print(f"Current Balance: {account.get_balance()}")
    account.print_transaction_history()
    print(account)